import transformers
from transformers import pipeline 

qna_model = pipeline("question-answering")

def extract(text, query):
    """
    highlights certain phrase from a text 
    """
    response = qna_model(context=text, question=query)
    return response['answer']
