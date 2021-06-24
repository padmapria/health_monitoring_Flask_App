# health_monitoring_Flask_App

Designing RESTful API with Python-Flask and MongoDB using health_monitoring dataset    

This example project demonstrate how to design RESTful API with Python-Flask and MongoDB.    

 You can download this project by cloning the repository:     

# Get the project code
git clone https://github.com/padmapria/health_monitoring_Flask_App.git    
NOTE: While working with Python, its recommended to use virtual environment to keep all the project's dependencies isolated from other projects.    

# To automate creating conda environment and deploying the project,
1) Clone this git repository in a folder, for example to the folder,  C:/health_monitoring 

2) Edit the startup.bat located in the scripts folder of this git project.
   Modify the venv_root_dir     
     set venv_root_dir="D:\health_monitoring_python\scripts"      
     to     
      set venv_root_dir="C:\health_monitoring\scripts"    
      
      save the changes
      
 3) Edit the start_app.bat located in the scripts folder of this git project. Modify the path pointing to the python file.      
      python D:\health_monitoring_python\app\TestPatientDetails.py     
      python D:\health_monitoring_python\app\patientDetails.py    
      
      to    
      python C:\health_monitoring\app\TestPatientDetails.py    
      python C:\health_monitoring\app\patientDetails.py    
      
      save the changes
      
  4) Run the startup.bat located in the scripts folder    
        
  The above steps will automatically   
        1) create a local conda environment    
        2) installing the dependencies given in the requirements.txt located in the scipts folder    
        3) Starting the unit test scripts to run    
        4) Starting the application   
      
## Test the application
Once the application is started, go to localhost on Postman to test the API.
 
select basic authentication and provide a valid username and password. Username and password should passed in the basic authentication to test all the 3 APIs.     
 
### To Test Authentication (Get Request)   
127.0.0.1:5000/rest-auth    

[![auth-postman.jpg](https://i.postimg.cc/1txqFfCP/auth-postman.jpg)](https://postimg.cc/GBQtwhnS)

### To get Summary (Post Request).    
The input payload should be passed via the request body. Use the request payload attached in this repository   
127.0.0.1:5000/summary    

[![summary-postman.jpg](https://i.postimg.cc/44VYDf8H/summary-postman.jpg)](https://postimg.cc/V5ssM8Pz)


### To get rank (Get Request)
127.0.0.1:5000/rank 

[![rank-postman.jpg](https://i.postimg.cc/tCrpf8HV/rank-postman.jpg)](https://postimg.cc/XpyRBHqV)

      
# To manually do the steps given in the steps 1 to 4, follow the below
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
Once the application is started, go to localhost on Postman to test the API, using the endpoint given above.

