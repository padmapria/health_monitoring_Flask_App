"""This module is to configure app to connect with database."""

from pymongo import MongoClient

#DATABASE = MongoClient()['empower-auth'] # DB_NAME
DEBUG = True
client = MongoClient('localhost', 27017)