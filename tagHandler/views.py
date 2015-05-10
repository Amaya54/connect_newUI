from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
from django.http import HttpResponse
import json
from dbUtils import *
from django.core import serializers
@csrf_exempt
# Create your views here.
def updateUserTags(request):
	userId = request.POST['userId']
	tags = request.POST['tags']
	print tags
	responseCode = updateTags(userId,tags)
	response = {'responseCode':responseCode}
	return HttpResponse(json.dumps(response), content_type="application/json")
