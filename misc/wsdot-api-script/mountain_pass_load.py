import requests
import configparser
import pandas as pd

# assign ConfigParser class from configparser module to parser variable
parser = configparser.ConfigParser()
# read is a method used on parser
parser.read("..\..\conf\pipeline.conf")

accesscode = parser.get("wsdot_api","access_code")

# create full url path w access code
url_base = 'http://wsdot.wa.gov/Traffic/api/MountainPassConditions/MountainPassConditionsREST.svc/GetMountainPassConditionsAsJson?AccessCode='
full_url = url_base + accesscode 

# get response and convert into json. json is a method
# use pandas to create a dataframe with flattened json data
api_response = requests.get(full_url)
json_data = api_response.json()
flattened_json = pd.json_normalize(json_data)

flattened_json.to_csv("pass.csv")
print(flattened_json)