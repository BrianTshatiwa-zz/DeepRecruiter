#from django.shortcuts import render
import os
import requests
from django.http import HttpResponse, response
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

# Create your views here.

@csrf_exempt
def message(request):
    user = request.POST.get('From')
    message = request.POST.get('Body')
    media_url = request.POST.get('MediaUrl0')
    print(f'{user} sent {message}')

    response = MessagingResponse()
    if media_url:
        r = requests.get(media_url)
        content_type = r.headers['Content-Type']
        username = user.split(':')[1]
        if content_type == 'audio/ogg':
            filename = f'uploads/{username}/{message}.ogg'
        else:
            filename = None
        if filename:
            if not os.path.exists(f'uploads/{username}'):
                os.mkdir(f'uploads/{username}')
            with open(filename, 'wb') as f:
                f.write(r.content)
            response.message('Thank you! Your voice message was recieved.')
        else:
            response.message('The file you submitted is not supported voice type.')
    else:
        response.message('Please send a voice note!')

    return HttpResponse('Hello!')

