from django.http import HttpResponse, response
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from .utils.emotion_extractor import get_emotion 
from .utils.intent_detector import get_intent
from .utils.recruiting_engine import ranking_model, DeepRecruiter
from .utils.verify_id import verify_id
from .utils.information_extractor import extract
from .models import Provider

RecruitingEngine = DeepRecruiter(ranking_model)

@csrf_exempt
def message(request):
    message = request.POST.get('Body')
    response = MessagingResponse()
    if get_intent(message) == "General_Greetings":
        response = MessagingResponse()
        response.message("Hello my name is DeepRecruiter, if you want a service type your problem and i will find for you the best person to help you. If you are instead a provider, type your full name, ID number, skills, abilities, hobbies, interests and phone number.")
   
    elif get_intent(message) == "General_Human_or_Bot":
        id_no = extract(message, "What is the identity number?")
        name = extract(message, "What is the full name?")
        skills = extract(message, "What are the skills?")
        hobbies = extract(message, "What are the hobbies?")
        interests = extract(message, "What are the interests?")
        abilities = extract(message, "What are the abilities?") 
        phone_number = extract(message, "What is the contact number or phone number?")
        provider = Provider(full_name=name, id_no=id_no, skills=skills, hobbies=hobbies, interests=interests, abilities=abilities, contact=phone_number)
        provider.save()
        response = MessagingResponse()
        response.message("I will link you up with someone who needs your services")
    else:
        response = MessagingResponse()
        response.message("Hang in there! I am looking for a person for you!")
        providers = Provider.objects.all()
        candidates = []
        for provider in providers:
            abilities = provider.skills + " " + provider.abilities + " " + provider.interests + " " + provider.hobbies
            cos_score = round(RecruitingEngine.compute_similarity(message, abilities))
            candidate = [provider.full_name, provider.contact, cos_score]
            candidates.append(candidate)
            response = MessagingResponse()
        candidate = (max([int(candidate) for candidate in candidates[0]]))
        response.message(f'Name: {candidate.full_name}, Score: {candidate.score}')
           
        #response.message(str(candidates))
    return HttpResponse(str(response))