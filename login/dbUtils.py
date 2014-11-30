from models import *
from django.db import IntegrityError, DatabaseError
from django.core.exceptions import ValidationError
from register.models import users

def loginUser(userName,password):
	user = ''
	try:
		if '@' in userName:
			user = login.objects.get(password = password, email = userName)	
		else:
			user = login.objects.get(password = password, contactNo = userName)
		user = users.objects.get(email = user.email,password = user.password, contactNo = user.contactNo)
		

	except login.DoesNotExist, e:
		print "Exception "+str(e)
		RESPONSE_CODE = "User not registered or Password is incorrect"
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