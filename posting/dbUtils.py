from models import *
from django.db import IntegrityError, DatabaseError
from django.core.exceptions import ValidationError
import uuid

def createPost(userId,title,content,filterBy,tags):
	try:
		user = postDetails(postId = uuid.uuid4(), title = title, content = content, filterBy = filterBy, tags = tags, userId = userId)
		user.save()
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
	return RESPONSE_CODE , "USER SAVED"


from django.core import serializers
def getPost(userId,filters):
	user = ''
	try:

		if filters == 'ALL':
			user = postDetails.objects.order_by('-dop')[:50]
		elif filters == 'ME':
			user = postDetails.objects.all().filter(userId = userId).order_by('-dop')[:50]
		else:
			filters = eval(filters);
			k = "%"+filters['search']+"%"
			user = postDetails.objects.extra(where=["tags like %s OR content like %s OR title like %s"], params =[k,k,k]).order_by('-dop') [:50]

	except postDetails.DoesNotExist, e:
		print "Exception "+str(e)
		RESPONSE_CODE = "Incorrect Parameters"
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
	return user,RESPONSE_CODE , "USER SAVED"