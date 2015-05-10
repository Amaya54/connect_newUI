from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
from django.http import HttpResponse
from register.models import *
from login.models import login
from django.db import IntegrityError, DatabaseError
from django.core.exceptions import ValidationError
import json
@csrf_exempt
def update(request):
	name = request.POST['name']
	userId = request.POST['userId']
	location = request.POST['location']
	contactNo = request.POST['contactNo']	
	fbUserName = request.POST['fbUserName']
	#tags = request.POST['tags']
	#fbUserName = "guest"

	try:
		user = users.objects.get(userId = userId)
		user.name = name
		user.location = location
		user.contactNo = contactNo
		user.fbUserName = fbUserName
		loginUser = login.objects.get(email = user.email)
		loginUser.contactNo = contactNo		
		user.save()
		loginUser.save()
	except users.DoesNotExist, e:
		print "Exception "+str(e)
		RESPONSE_CODE = "User DoesNotExist"
	except ValidationError, e:
		print "Exception "+str(e)
		RESPONSE_CODE = "RESPONSE_CODE_VALIDATION_ERROR"
	except IntegrityError, e:
		print "Exception "+str(e)
		RESPONSE_CODE = "RESPONSE_CODE_INTEGRITY_ERROR"		
	except DatabaseError, e:
		print "Exception "+str(e)
		RESPONSE_CODE = "RESPONSE_CODE_DATABASE_ERROR"
	except Exception, e:
		print "Exception "+str(e)
		RESPONSE_CODE = "RESPONSE_CODE_GENERIC_ERROR"
	else :
		RESPONSE_CODE = "RESPONSE_CODE_SUCCESS"
	response = {'responseCode':RESPONSE_CODE}
	return HttpResponse(json.dumps(response), content_type="application/json")