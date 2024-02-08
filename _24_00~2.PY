import json
from datetime import datetime
import requests
import os
import time

gender = "male"
weight_in_kg = "75.8"
height_in_cm = "179"
age = 40

#Encrypt the following in Env Vars:

# Toggle off or on, depending on Commiting or not: (if toggled off for the actual password, then toggle on the Env Vars and ensure Env Vars work, then just remove your actual password entirely from the code:

# APP_ID = (< enter hidden Value in Env Var Field, without spaces or quotes >)
APP_ID = os.environ.get('APP_ID')
print(f"The APP_ID is: {APP_ID}")

# Toggle off or on, depending on Commiting or not: (if toggled off for the actual password, then toggle on the Env Vars and ensure Env Vars work, then just remove your actual password entirely from the code:
# API_KEY = (<enter hidden Value in Env Var Field, without spaces or quotes>)
API_KEY = os.environ.get('API_KEY')
print(f"The API_KEY is: {API_KEY}")

# Toggle off or on, depending on Commiting or not: (if toggled off for the actual password, then toggle on the Env Vars and ensure Env Vars work, then just remove your actual password entirely from the code:
# AUTHORIZATION_BEARER_TOKEN = (<enter hidden Value in Env Var Field, without spaces or quotes>)
AUTHORIZATION_BEARER_TOKEN = os.environ.get('AUTHORIZATION_BEARER_TOKEN')
print(f"The AUTHORIZATION_BEARER_TOKEN is: {AUTHORIZATION_BEARER_TOKEN}")


#------------------ Nutritionix Territory -----------------#
# host domain: https://trackapi.nutritionix.com
exercise_endpoint_url = "https://trackapi.nutritionix.com/v2/natural/exercise"   #MY ACTUAL ENDPOINT.

#-----------------  Sheety Territory -----------------#
# SHEETY_ENDPOINT_URL =  = (<enter hidden Value in Env Var Field, without spaces or quotes>)
# Toggle off or on, depending on Commiting or not: (if toggled off for the actual password, then toggle on the Env Vars and ensure Env Vars work, then just remove your actual password entirely from the code:
SHEETY_ENDPOINT_URL = os.environ.get('SHEETY_ENDPOINT_URL')
print(f"The SHEETY_ENDPOINT_URL is: {SHEETY_ENDPOINT_URL}")


# to use bearer Tokens:
sheety_headers = {
    "Authorization": f"Bearer {AUTHORIZATION_BEARER_TOKEN}",
    "Content-Type": "application/json"
}

exercise_text = input("Please tell me which exercises you did Today, and the duration of each (if you know): ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
print(APP_ID)
print(API_KEY)


parameters = {
    "query": exercise_text,
    "gender": gender,
    "weight_kg": weight_in_kg,
    "height_cm": height_in_cm,
    "age": age,
}

exercise_response = requests.post(url=exercise_endpoint_url, json=parameters, headers=headers)
exercise_result = exercise_response.json()
print(exercise_result)

#{"exercises":[{"tag_id":63,"user_input":"swam","duration_min":60,"met":6,"nf_calories":420,"photo":{"highres":"https://d2xdmhkmkbyw75.cloudfront.net/exercise//63_highres.jpg","thumb":"https://d2xdmhkmkbyw75.cloudfront.net/exercise//63_thumb.jpg","is_user_uploaded":false},"compendium_code":18310,"name":"swimming","description":null,"benefits":null}]}


date_and_time_now = datetime.now()
print(date_and_time_now)

now_formatted_date = date_and_time_now.strftime("%d/%m/%Y")
print(now_formatted_date)

now_formatted_time = date_and_time_now.strftime("%H:%M:%S")   #same thing as: print(date_and_time_now.strftime("%X"))
print(now_formatted_time)


# TODO1: You will be using strftime()

# TODO: APIs and Making POST Requests

# TODO: Authorization Headers

# TODO: Environment Variables


# Tip: You could do this approach:
'''
exercises = exercise_result['exercises']
for exercise in exercises:
    json_payload_sheet_inputs = {
        "workout": {
'''

# OR you could do this:

for each_exercise in exercise_result['exercises']:  # exercises = exercise_result['exercises']
    # time.sleep(1)
    json_payload_sheet_inputs = {
        'workout' : {
            "date" : now_formatted_date,
            "time" : now_formatted_time,
            "exercise": each_exercise['name'].title(),
            "duration": each_exercise['duration_min'],  # in minutes
            "calories": each_exercise['nf_calories'],  # in kcal
        }
    }
    sheety_post_request_response = requests.post(url=SHEETY_ENDPOINT_URL, json=json_payload_sheet_inputs, headers=sheety_headers)
    print(sheety_post_request_response.text)