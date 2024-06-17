# Use watsonx, and `granite-20b-multilingual` to support multiple languages translation

**Disclaimers**
The goal of this repository is to show the capabilities of WatsonX ML using the `granite-20b-multilingual` to demonstrate how to translate multiple languages.

This repository is based on [Mateusz Szewczyk's](https://github.com/IBM/watson-machine-learning-samples/blob/master/cloud/notebooks/python_sdk/deployments/foundation_models/Use%20watsonx%2C%20and%20%60granite-20b-multilingual%60%20to%20support%20multiple%20languages%20translation.ipynb) repository.

**Requirements**
1. Create a [Watson Machine Learning (WML) Service instance](https://cloud.ibm.com/catalog/services/watson-machine-learning) (a free plan is offered and information about how to create the instance can be found [here](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/wml-plans.html?context=wx&audience=wdp)).
2. Install `ibm-watsonx-ai` dependecies:
  ```
  $ pip install "ibm-watsonx-ai"
  ```
3. Edit `example.env.py` file with your IBM Cloud API Key, and watsonx Project ID.
4. Rename the file `example.env.py` to `env.py`.
5. Run the script:
  ```
  $ python3 main.py
  ```