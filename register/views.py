from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
from django.http import HttpResponse
from dbUtils import createUser
import json
@csrf_exempt
def register(request):
	name = request.POST['name']
	dob = request.POST['dob']
	location = request.POST['location']
	gender = request.POST['gender']
	email = request.POST['email']
	contactNo = request.POST['contactNo']
	flags = request.POST['flags']
	password = request.POST['password']	
	responseCode, responseString = createUser(name,password,dob,location,gender,email,contactNo,flags)
	response = {'responseCode':responseCode}
	return HttpResponse(json.dumps(response), content_type="application/json")