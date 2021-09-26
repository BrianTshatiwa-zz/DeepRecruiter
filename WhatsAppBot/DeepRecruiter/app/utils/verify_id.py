import requests
import json

def verify_id(identity_number: str):

   """
   interface for id verification
   Args:
     identity_number (str): 13 digit identity number 
   """

   url = "https://mtntadhack2021.contactable.co.za/api/validation"

   payload = json.dumps(identity_number)
   headers = {
   'Authorization': 'Basic bXRuX3RhZF91c2VyOmFjNGI4N2YyLTFhMGQtNDkwNi05ZGM5LTFjMGMxNTVhODA0Yw==',
   'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, data=payload, verify=False)
   return response