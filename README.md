# health_monitoring_Flask_App

Designing RESTful API with Python-Flask and MongoDB using health_monitoring dataset    

This example project demonstrate how to design RESTful API with Python-Flask and MongoDB.    

 You can download the project this project by cloning the repository:     

# Get the project code
git clone https://github.com/padmapria/health_monitoring_Flask_App.git    
NOTE: While working with Python, its recommended to use virtual environment to keep all the project's dependencies isolated from other projects.    

## Create your local environment    
conda init
conda create -n health_monitoring python=3.7 anaconda     # To create the environment    
activate health_monitoring     # To activate the environment    

## Install dependencies    
pip install -r requirements.txt    
Start MongoDB Server    
    
## Config the application and deploy the application    
Change the DBNAME in the config file according to the database name you are using.    

Start the application to test locally using the below command  
python patientDetails.py    

## Test the application    
Once the application is started, go to localhost on Postman to test the API.

To Test Authentication          
127.0.0.1:5000/rest-auth       

To get Summary     
127.0.0.1:5000/get_summary    

To get rank

