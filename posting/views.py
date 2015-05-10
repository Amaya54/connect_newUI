from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
from django.http import HttpResponse
from dbUtils import *
import json
from django.core import serializers
from register.models import *
@csrf_exempt
def post(request):
	userId = request.POST['userId']
	title = request.POST['title']
	content = request.POST['content']
	filterBy = request.POST['filterBy']
	tags = request.POST['tags']	
	responseCode, responseString = createPost(userId,title,content,filterBy,tags)
	response = {'responseCode':responseCode}
	return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def fetchPost(request):
	userId = request.POST['userId']
	filters = request.POST['filters']
	name = location = fbUserName = contactNo =''
	if filters == 'USER':
		userDetails,responseCode = getUserDetails(userId,'name')
		if userDetails !='':
			userId = userDetails.userId
			name = userDetails.name
			location = userDetails.location
			contactNo = userDetails.contactNo
			fbUserName = userDetails.fbUserName
	user, responseCode, responseString = getPost(userId,filters)  
	user = serializers.serialize("json", user)                               
	data = json.loads(user)
	for each in data:
		each.pop('model')
		each['fields']['postId'] = each['pk']
		each.pop('pk')
		userDetails,responseCode = getUserDetails(each['fields']['userId'],'id')
		if userDetails !='':
			each['fields']['name']= userDetails.name
			each['fields']['location']= userDetails.location
			each['fields']['contactNo'] = userDetails.contactNo
			each['fields']['fbUserName'] = userDetails.fbUserName


	if len(data) > 0:
		data[0]['fbUserName'] = fbUserName
		data[0]['location'] = location
		data[0]['contactNo'] = contactNo
		data[0]['name'] = name
	return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def getUserDetails(userId,type):
	user =''
	try:
		if type == 'name':
			user = users.objects.get(name = userId)
		else:
			user = users.objects.get(userId = userId)		
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
	return user,RESPONSE_CODE