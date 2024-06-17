import getpass
import os
from ibm_watsonx_ai.foundation_models import get_model_specs
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods
from ibm_watsonx_ai.foundation_models import ModelInference
from env import *

## Endpoints ML WatsonX
## London "url": "https://eu-gb.ml.cloud.ibm.com"
## Frankfurt "url": "https://eu-de.ml.cloud.ibm.com"
## Dalas "url": "https://us-south.ml.cloud.ibm.com"

## Defining the WML Credentials
credentials = {
  "url": "https://eu-gb.ml.cloud.ibm.com",
  "apikey": API_KEY
}

## Defining the project id
try:
  project_id = PROJECT_ID
except KeyError:
  project_id = input("Please enter your project_id (hit enter): ")

## List available models on Watson ML
models = get_model_specs(credentials["url"])["resources"]
model_ids = [model["model_id"] for model in models]

## Print each model ID on a single line
#for model_id in model_ids:
#  print(model_id)

## Choose your model
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

## Print Model Details
#print(model.get_details())

## Translation Text based a Query
english_to_spanish_query = """Translate the following text from English to Spanish:

Input: So far, I have not been terribly encouraged by the stance adopted by the Commission.
Output: Hasta ahora no me ha animado mucho la postura adoptada por la Comisión.

Input: I am very pleased to see that the joint resolution adopts the suggestion we made.
"""

## Translation Result from Query
translation_result = model.generate_text(english_to_spanish_query)

## Print Result
print(translation_result)

