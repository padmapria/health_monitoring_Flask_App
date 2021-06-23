# health_monitoring_Flask_App

Designing RESTful API with Python-Flask and MongoDB using health_monitoring dataset
This example project demonstrate how to design RESTful API with Python-Flask and MongoDB.

First you'll need to get the source of the project. You could do this by cloning the repository:

# Get the project code
git clone https://github.com/padmapria/health_monitoring_Flask_App.git
NOTE: While working with Python, its recommended to use virtual environment to keep all the project's dependencies isolated from other projects.

Create your local environment
conda create -n health_monitoring python=3.7 anaconda # To create the environment
activate health_monitoring # To activate the environment
Install dependencies
pip install -r requirements.txt
Start MongoDB Server

Config the application
Change the DBNAME in the config file according to the database name you are using.

Start the application to test locally
python patientDetails.py
Once the application is started, go to localhost on Postman and explore the APIs.
