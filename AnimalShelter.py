from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
	""" CRUD operations for Animal colleciton in MongoDB """

	def __init__(self, username, password):
		# Initialize MongoClient
		self.client = MongoClient('mongodb://%s:%s@localhost:37303' % (username, password), authSource='AAC')
		# Retrieve database from mongodb client
		self.database = self.client['AAC']

	""" Create """
	def create(self, data):
		if data is not None:
			return self.database.animals.insert_one(data).acknowledged
		else:
			raise Exception("Error (AnimalShelter.create(...)): 'data' paramter is empty")

		return False

	""" Read """
	def read(self, query):
		if query is None:
			# an empty query returns all documents in collection
			query = {}
		
		return self.database.animals.find(query, {"_id":False})

	""" Update """
	def update(self, query, data):
		if query is None:
			# an empty query updates all documents in collection
			query = {}

		if data is not None:
			return self.database.animals.update_many(query, data)
		else:
			raise Exception("Error (AnimalShelter.update(...)): 'data' paramter is empty")

	""" Delete """
	def delete(self, query):
		if query is None:
			# an empty query deletes all documents in collection
			query = {}
		
		return self.database.animals.remove(query)
