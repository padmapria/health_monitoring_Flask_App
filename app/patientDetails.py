"""
patientDetails: 
"""
from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from config import client
from PatientSummary import PatientSummary  

app = Flask(__name__)    # Construct an instance of Flask class for our webapp)

#Enable basic Authentication
auth = HTTPBasicAuth()

# Select the database
db = client["empower-auth"]

# Select the collection
patient_collection = db.patient
daily_activity=db.daily_activity_summary 

#Declaring the global variable to set Authenticated user as default user
user_id=None
    
'''
    method to fetch userdetails authentication
'''
@auth.verify_password
def authenticate(username, password):
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
        
if __name__ == '__main__':  # Script executed directly?
    app.run()  # Launch built-in web server and run this Flask webapp