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
		posterId =post.userId
		if userId == posterId:
			RESPONSE_CODE = 'RESPONSE_CODE_SAME_USER'
			return RESPONSE_CODE
		flag1 = eval(post.filterBy)['flag']
		post.connectCount = post.connectCount + 1
		post.save()
		user = users.objects.get(userId = userId)
		flag2 = user.flags[1:]
		print flag1
		print flag2
		flag = flag2 +""+ flag1
		print flag1+" "+flag2	 	
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
	if exchangeFlag == '0001':
		return 'Send Poster Mailid to Connector'
	elif exchangeFlag == '0010':
		return 'Send Poster contactNo to Connector'
	elif exchangeFlag == '0011':
		return 'Send Poster Mail,contactNo to Connector'
	elif exchangeFlag == '0100':
		return 'Send Connector Mailid to Poster'
	elif exchangeFlag == '0101':
		return 'Send Connector Mailid to Poster and Send Poster Mailid to Connector'
	elif exchangeFlag == '0110':
		return 'Send Connector Mailid to Poster and Send Poster contactNo to Connector'
	elif exchangeFlag == '0111':
		return 'Send Connector Mailid to Poster and Send Poster Mailid,contactNo to Connector'
	elif exchangeFlag == '1000':
		return 'Send Connector contactNo to Poster'
	elif exchangeFlag == '1001':
		return 'Send Connector contactNo to Poster and Send Poster Mailid to Connector'
	elif exchangeFlag == '1010':
		return 'Send Connector contactNo to Poster and Send Poster contactNo to Connector'
	elif exchangeFlag == '1011':
		return 'Send Connector contactNo to Poster and Send Poster contactNo,Mailid to Connector'
	elif exchangeFlag == '1100':
		return 'Send Connector contactNo,Mailid to Poster'
	elif exchangeFlag == '1101':
		return 'Send Connector contactNo,Mailid to Poster and Send Poster Mailid to Connector'
	elif exchangeFlag == '1110':
		return 'Send Connector contactNo,Mailid to Poster and Send Poster contactNo to Connector'
	elif exchangeFlag == '1111':
		return 'Send Connector contactNo,Mailid to Poster and Send Poster contactNo,Mailid to Connector'



def getConnected(userId,postId):
	data = ''
	try:
		user = connectDetails.objects.get(userId = userId, postId = postId)
		return 'RESPONSE_CODE_ALREADY_CONNECTED','You are already connected with this post'
	except connectDetails.DoesNotExist:
		exchangeFlag = exchange(userId,postId)
		if exchangeFlag == 'RESPONSE_CODE_SAME_USER':
			return 'RESPONSE_CODE_SAME_USER','You cannot connect with yourself'
		user = connectDetails(connectId = uuid.uuid4(), userId = userId, postId = postId, exchangeFlag = exchangeFlag)
		user.save()
		data = exchangeInfo(exchangeFlag)
		RESPONSE_CODE = "RESPONSE_CODE_SUCCESS"
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
	return RESPONSE_CODE , data

