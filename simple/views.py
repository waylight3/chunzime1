#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from watson_developer_cloud import DocumentConversionV1
from watson_developer_cloud import ConversationV1
import json, os

def index(request):
    data = {}
    return render(request, 'simple/index.html', data)

def home(request):
    data = {}
    return render(request, 'simple/home.html', data)

# ajax로 conversation api를 연동하기 위한 함수
def conversation(request):

    # get 요청의 경우
    if request.method == 'GET':
        
        # api 신임 정보 입력
        conversation = ConversationV1(
                username='e50bf787-668b-4756-824a-6ad1e8d33912',
                password='68xg1yDhpQOr',
                version='2016-09-20'
                )
        
        # 문맥 불러오기
        context = json.loads(request.GET.get('context', '{}'))
        
        # 저장소 지정
        workspace_id = '95e19486-e402-4c2b-9007-b0b36be7b066'
        
        # api 호출
        response = conversation.message(
                workspace_id=workspace_id,
                message_input={'text': request.GET['message']},
                context=context
                )
        
        # 클라이언트로 응답 반환
        data = {'answer':response['output']['text'], 'context':response['context']}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')

    # api 응답에 실패한 경우 fail 반환
    data = {'answer':'fail'}
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')