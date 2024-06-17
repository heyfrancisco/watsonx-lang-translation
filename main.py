import getpass
import os
from ibm_watsonx_ai.foundation_models import get_model_specs
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods
from ibm_watsonx_ai.foundation_models import ModelInference
from env import PROJECT_ID, API_KEY

## Defining API KEY
try:
  API_KEY = API_KEY
except KeyError:
  API_KEY = input("Please enter your API_KEY (hit enter): ")

endpoints = {
  1: {"name": "London", "url": "https://eu-gb.ml.cloud.ibm.com"},
  2: {"name": "Frankfurt", "url": "https://eu-de.ml.cloud.ibm.com"},
  3: {"name": "Dallas", "url": "https://us-south.ml.cloud.ibm.com"}
}

print("Available Endpoints WatsonX")
for key, endpoint in endpoints.items():
    print(f"{key}. {endpoint['name']} \"url\": \"{endpoint['url']}\"")

# Prompt the user to select an endpoint by number
selected_number = int(input("\nChoose your endpoint location: "))

# Validate the user input
if selected_number in endpoints:
    selected_endpoint = endpoints[selected_number]
else:
    print("Invalid selection. Please run the script again and select a valid number.")
    exit(1)

credentials = {
    "url": selected_endpoint["url"],
    "apikey": API_KEY
}

## Defining the project id
try:
  project_id = PROJECT_ID
except KeyError:
  project_id = input("Please enter your project_id (hit enter): ")

## Choose your model
### To find more models: 
### models = get_model_specs(credentials["url"])["resources"]
### model_ids = [model["model_id"] for model in models]
model_id = "ibm/granite-20b-multilingual"

## Defining the model parameters
parameters = {
    GenParams.DECODING_METHOD: DecodingMethods.SAMPLE,
    GenParams.MAX_NEW_TOKENS: 100,
    GenParams.MIN_NEW_TOKENS: 1,
    GenParams.TEMPERATURE: 0.5,
    GenParams.TOP_K: 50,
    GenParams.TOP_P: 1,
    GenParams.STOP_SEQUENCES: ["\n"]
}

model = ModelInference(
  model_id=model_id,
  params=parameters,
  credentials=credentials,
  project_id=project_id
)

# Function to prompt the user for input text
def get_user_input():
    return input("Enter the text you want to translate from English to Spanish: ")

user_input_text = get_user_input()

english_to_spanish_query = f"""Translate the following text from English to Spanish:

Input: So far, I have not been terribly encouraged by the stance adopted by the Commission.
Output: Hasta ahora no me ha animado mucho la postura adoptada por la Comisión.

Input: {user_input_text}
Output:
"""


## Translation Result from Query
translation_result = model.generate_text(english_to_spanish_query)

## Print Result
print("\nTranslation Result:")
print(translation_result)