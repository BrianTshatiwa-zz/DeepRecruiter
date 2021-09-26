from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('LpSsKfmftL_uY9YwZaU0EB1loon452SRqKcIzSf-1FtT')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator=authenticator
)

assistant.set_service_url('https://api.au-syd.assistant.watson.cloud.ibm.com/instances/a0af3ba6-dd17-4c32-8c68-7baf4be258da')

def get_intent(text):
    """
    an interface for detecting intent
    Args:
      text (str): greeting or anything 
    """
    response = assistant.message_stateless(
        assistant_id='b9d51a2d-ee20-479a-ad6f-cebfc4661f0e', 
        input={
            'message_type':'text',
            'text':text
        }
    ).get_result()
    return response['output']['intents'][0]['intent']