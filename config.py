#!
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY 						= 'myprecious'
	# SQLALCHEMY_DATABASE_URI 		= 'mysql://root:''@localhost/builtapi'
	SQLALCHEMY_DATABASE_URI 		= 'mysql://drew:secret@db/builtapi'
	SQLALCHEMY_TRACK_MODIFICATIONS 	= False
	KINESIS_DATA_STREAM 			= 'TestStream'
	AWS_REGION 						= 'us-east-1'