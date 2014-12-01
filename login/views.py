import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
from django.http import HttpResponse
from dbUtils import loginUser
@csrf_exempt
def login(request):
	userName = request.POST['userName']
	password = request.POST['password']	
	user, responseCode, responseString = loginUser(userName,password)
	if user != '':
		user.__dict__.pop('doj')
		user.__dict__.pop('_state')
		user.__dict__.pop('password')
		user.__dict__['responseCode'] = responseCode
		return HttpResponse(json.dumps(user.__dict__), content_type="application/json")
	else:
		response = {'responseCode':responseCode}
		return HttpResponse(json.dumps(response), content_type="application/json")

