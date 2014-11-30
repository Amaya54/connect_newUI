from models import *
from login.models import login
from django.db import IntegrityError, DatabaseError
from django.core.exceptions import ValidationError
import uuid

def createUser(name,password,dob,location,gender,email,contactNo,flags):
	try:
		user = users(userId = uuid.uuid4(), name = name, password = password, location = location, dob = dob, gender = gender, email = email, contactNo = contactNo, flags = flags)
		loginUser = login(email=email, contactNo = contactNo, password = password)
		user.save()
		loginUser.save()		
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
