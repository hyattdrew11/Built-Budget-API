#!
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY 						= 'myprecious'
	SQLALCHEMY_DATABASE_URI 		= 'mysql://root:''@localhost/builtapi'
	SQLALCHEMY_TRACK_MODIFICATIONS 	= False