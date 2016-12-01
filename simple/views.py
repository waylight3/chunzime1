from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from watson_developer_cloud import DocumentConversionV1
from watson_developer_cloud import ConversationV1
import json, os

def index(request):
    conversation = ConversationV1(
            username='e50bf787-668b-4756-824a-6ad1e8d33912',
            password='68xg1yDhpQOr',
            version='2016-09-20'
            )
    context = {}
    workspace_id = '95e19486-e402-4c2b-9007-b0b36be7b066'
    response = conversation.message(
            workspace_id=workspace_id,
            message_input={'text': 'Tell me what is earthquake prevention'},
            context=context
            )
    data = {'answer':response}
    return render(request, 'simple/index.html', data)

def home(request):
    data = {}
    return render(request, 'simple/home.html', data)

def conversation(request):
    print('!!!! %s !!!!!' % request)
    try:
        if request.method == 'POST':
            message = request.POST['message']
            data = {'answer':'you said "%s".' % message}
            json_data = json.dumps(data)
            return HttpResponse(json_data, content_type='application/json')
    except:
        data = {'answer':'fail'}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
    data = {'answer':'fail'}
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')