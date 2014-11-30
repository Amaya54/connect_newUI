from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
from django.http import HttpResponse
from dbUtils import *
import json
from django.core import serializers
@csrf_exempt
def post(request):
	userId = request.POST['userId']
	title = request.POST['title']
	content = request.POST['content']
	filterBy = request.POST['filterBy']
	tags = request.POST['tags']	
	responseCode, responseString = createPost(userId,title,content,filterBy,tags)
	return HttpResponse(responseCode)

@csrf_exempt
def fetchPost(request):
	userId = request.POST['userId']
	filters = request.POST['filters']
	user, responseCode, responseString = getPost(userId,filters)  
	user = serializers.serialize("json", user)                                
	data = json.loads(user)
	for each in data:
		each.pop('model')
		each.pop('pk')
	return HttpResponse(json.dumps(data), content_type="application/json")