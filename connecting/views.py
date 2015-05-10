from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
from django.http import HttpResponse
from dbUtils import *
import json
from django.core import serializers
@csrf_exempt
def connect(request):
	userId = request.POST['userId']
	postId = request.POST['postId']
	#if userId == postId :
	#	response = {'responseCode':'RESPONSE_CODE_GENERIC_ERROR', 'responseString':'You cannot connect with yourself'}	
	#	return HttpResponse(json.dumps(response), content_type="application/json")		
	responseCode, responseString = getConnected(userId,postId)
	response = {'responseCode':responseCode, 'responseString':responseString}
	return HttpResponse(json.dumps(response), content_type="application/json")