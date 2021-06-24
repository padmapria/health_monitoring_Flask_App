"""
patientDetails: 
"""
from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from config import client
from PatientSummary import PatientSummary  
from bson.json_util import dumps
import ast,json
from datetime import datetime
import os # for Cwd path 
path = os.getcwd()
import logging
#from dateutil import parser

app = Flask(__name__)    # Construct an instance of Flask class for our webapp)

#Logs are generated in a seperate log folder
def level_down(path):
    proj_path= os.path.split(path)[0]
    log_dir=os.path.join(proj_path, 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return log_dir
    
logFormatStr = '%(asctime)s  %(levelname)s - %(message)s'
logging.basicConfig(filename=level_down(path) + '\logFile.log', format=logFormatStr, level=logging.INFO), logging.info('Application started')


#Enable basic Authentication
auth = HTTPBasicAuth()

# Select the database
db = client["empower-auth"]

# Select the collection
patient_collection = db.patient
daily_activity=db.daily_activity_summary 

#Declaring the global variable to set Authenticated user as default user
user_id=None
    
@auth.verify_password
def authenticate(username, password):
    logging.info('Test logging authenticate for every rest call')
    if username and password:
        myquery2= ({"username": username, "password": password})
        patient_record_fetched = patient_collection.find_one(myquery2)
        if(patient_record_fetched is None):
            print("Unauthorized user.. Username or password incorrect !!!!")
            return False
        else:
            print("User Authenticated ..")
            global user_id
            user_id=patient_record_fetched["_id"]
            return True
        
'''
    utility method to test authentication
'''
@app.route('/rest-auth')
@auth.login_required
def get_response():        
    return "Hello, %s!" % auth.current_user()
        

'''
    Rest Endpoint to get patient Summary
'''
#https://stackoverflow.com/questions/25015711/time-data-does-not-match-format
@app.route('/summary', methods=['POST'])
@auth.login_required
def get_summary():         # URL '/' to be handled by main() route handler
   
    print("******** Fetching the daily activity summary for the user ", user_id)
    body = ast.literal_eval(json.dumps(request.get_json()))
    print("Summary requested for ",body)
    
    dt = datetime.strptime(body['date'], '%Y-%m-%d')   
    
    '''Not working included for reference
        y =datetime.datetime.strptime(body['date'], '%Y-%m-%d')
        print(type(y)," ",y)
        z = parser.parse(body['date'])
        print(type(z)," ",z)
    '''
    
    #Passing the date requested from postman along with the user details of the logged user
    daily_summary=daily_activity.find_one({"patient": user_id, "date": datetime(dt.year, dt.month, dt.day, 0, 0)})
    
    if(daily_summary is None):
        return "User details not found for the given date"     
    else:
        for i in daily_summary:
            print(i, "= ", daily_summary[i])
        
        obj = PatientSummary(daily_summary['steps'],daily_summary['distance'],daily_summary['calories'],daily_summary['duration'] )
        print("******** Fetched the daily activity summary")
        return json.dumps(obj, default=obj2Json_summary) 
        
'''
    Rest Endpoint to get patient list in the descending order based on the total steps accumulated
'''       
#https://dba.stackexchange.com/questions/243947/join-two-collections-with-group-by-and-sum-in-mongodb
#https://stackoverflow.com/questions/42273228/join-and-sort-data-in-mongodb-php
@app.route('/rank')
@auth.login_required
def get_rank():         # URL '/' to be handled by main() route handler
    
    print("##### Fetching the total steps for all the users in descending order")
    output = []
    agg_result= daily_activity.aggregate(
    [{
    "$lookup" : 
        {"from":"patient",
         "localField":"patient",
         "foreignField":"_id",
         "as":"patientDetails"
        }
    },
    {   
        "$unwind":"$patientDetails"
    }, 
    {    
    "$group" : 
        {"_id" : "$patientDetails.username", 
         "num_steps" : 
            {
                "$sum" : "$steps" }
            }
        },
        {
            "$sort" : { "num_steps" : -1 }
        }
        
    ])
    
    for i in agg_result:
        print(i)
        output.append(i["_id"])
        
    print("##### Fetched the total steps for "+ str(len(output)) +" users")

    return dumps(output)


#utility method to convert object to json
def obj2Json_summary(obj):
    return {
        "steps": obj.steps,
        "distance": obj.distance, 
        "calorieBurn":obj.calorieBurn,
        "activeMins": obj.activeMins
        }
    
if __name__ == '__main__':  # Script executed directly?
    app.run()  # Launch built-in web server and run this Flask webapp
