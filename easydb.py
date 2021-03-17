import os
import pickle
import json

class EasyDB:
	def __init__(self, location="db"):
		self.location_raw = location
		if location != ":memory:":
			self.location = location + ".edb"
			if os.path.exists(self.location):
				try:
					self.db = json.loads(pickle.load(open(self.location,"rb")))
				except:
					self.db = {}
			else:
				open(self.location, 'a').close()
				self.db = {}
				pickle.dump(self.db, open(self.location, "wb"))
		else:
			self.db = {}

	def add(self, key, value):
		self.db.update({key:value})
		if self.location_raw != ":memory:":
			os.remove(self.location)
			pickle.dump(self.db, open(self.location, "wb"))

	def get(self, key):
		return self.db[key]

	def object(self):
		return self.db

	def delete(self, key):
		del self.db[key]
		if self.location_raw != ":memory:":
			os.remove(self.location)
			pickle.dump(self.db, open(self.location, "wb"))

	def add_dict(self, dict):
		self.db.update(dict)
		if self.location_raw != ":memory:":
			os.remove(self.location)
			pickle.dump(self.db, open(self.location, "wb"))
