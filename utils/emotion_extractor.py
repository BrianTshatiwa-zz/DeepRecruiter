import json 
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, EntitiesOptions

authenticator = IAMAuthenticator('AjKlf0_xCdHgGtBau7lhw3O4pNZRa-XdO7tRbH8DVziP')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)
natural_language_understanding.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/fa589d70-733d-4dc3-8a16-caa0621b6b08')

def get_emotion(text):
    """
    an interface for extracting emotions from a text
    Args: 
       text (str): Any text 
    """
    response = natural_language_understanding.analyze(
        text=text, 
        features=Features(sentiment=SentimentOptions())
    ).get_result()
    emotion = response['sentiment']['document']['label']
    return emotion