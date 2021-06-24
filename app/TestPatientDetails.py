from base64 import b64encode    
import json
'''
headers = {'Authorization': 'Basic ' + b64encode("{0}:{1}".format(username, password))}
rv = self.app.get('/path', headers=headers)
'''
import unittest
from patientDetails import app

class TestPatientDetails(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    #https://stackoverflow.com/questions/30249082/python-flask-test-client-doesnt-have-request-authorization-with-pytest
    def test_Auth(self):
        print("Testing Authentication ****")
        credentials = b64encode(b"max:max").decode('utf-8')
        response = self.app.get("/rest-auth", headers={"Authorization": f"Basic {credentials}"})
        self.assertEqual(response.status_code, 200)
        print()       
        
    
    def test_summary(self):
        print()
        print("Testing summary !!!!!!");
        credentials = b64encode(b"max:max").decode('utf-8')
        data = {
            "date": "2021-5-22"
        }

        response = self.app.post(
            "/summary",
            data=json.dumps(data),
            headers={"Authorization": f"Basic {credentials}", "Content-Type": "application/json"},
        )
        
        self.assertEqual(200, response.status_code)
        
        print("Summary response from test !!!!!",response.data)
        print("After eval **********",eval(response.data))
        
        #https://stackoverflow.com/questions/39491420/python-jsonexpecting-property-name-enclosed-in-double-quotes
        #Used eval to compare the results, so that the attributes are printed with single quotes
        
        self.assertEqual(eval(response.data),test_summary_obj)
        
    
    def test_rank(self):
        print("Testing Rank !!!!");
        credentials = b64encode(b"max:max").decode('utf-8')
        response = self.app.get("/rank", headers={"Authorization": f"Basic {credentials}"})
        print("Rank response from test !!!!! ",response.data)
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(len(eval(response.data)), 79)
       

test_summary_obj= {"steps": 0, "distance": 0.0, "calorieBurn": 1466, "activeMins": 0}

if __name__ == '__main__':
    unittest.main()