from models import *
from django.db import IntegrityError, DatabaseError
from django.core.exceptions import ValidationError
import uuid
from posting.models import * 
from register.models import *

def exchange(userId,postId):
	flag = ''
	try:
		post = postDetails.objects.get(postId = postId)
		flag1 = eval(post.filterBy)['flag']
		user = users.objects.get(userId = userId)
		flag2 = user.flags[1:]
		flag = flag2 + flag1 		
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
		RESPONSE_CODE = flag
	return RESPONSE_CODE
	
def exchangeInfo(exchangeFlag):
	if exchangeFlag == '1111':
		print 'Exchange all info among all'
	elif exchangeFlag == '1110':
		print 'Connecter all Poster only mobile'
	elif exchangeFlag == '1101':
		print 'Connecter all Poster only email'
	elif exchangeFlag == '1011':
		print 'Connector only mobile Poster all'
	elif exchangeFlag == '0111':
		print 'Connecter only mail Poster all'
	elif exchangeFlag == '1100':
		print 'Exchange all info among all'
	elif exchangeFlag == '1001':
		print 'Exchange all info among all'




def getConnected(userId,postId):
	try:
		exchangeFlag = exchange(userId,postId)
		user = connectDetails(connectId = uuid.uuid4(), userId = userId, postId = postId, exchangeFlag = exchangeFlag)
		user.save()
		exchangeInfo(exchangeFlag)
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

