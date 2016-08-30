from django.conf import settings
from pymongo import MongoClient
import re

def dbConnect():
    # Database properties
    dbName = settings.DATABASES['default']['NAME']
    dbPort = int(settings.DATABASES['default']['PORT'])
    dbHost = settings.DATABASES['default']['HOST']
    dbHost = dbHost if not dbHost == '' else 'localhost'
    # Connect
    client = MongoClient(dbHost, port=dbPort)
    db = client[dbName]
    return db

def extractUserId(user_email):
    user_id, rest = re.split('@', user_email)
    return user_id
