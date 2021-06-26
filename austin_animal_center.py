from pymongo import MongoClient
from bson.json_util import dumps

class AustinAnimalCenter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:45665/default_db?authSource=AAC' % (username, password))
        self.database = self.client['AAC']

    # Create method to implement the C in CRUD.
    # data: Fields and values to create new document (Must be a dictionary)
    # Returns True if insert is successful or False otherwise
    # Raises exception if data is None
    def create(self, data):
        if data is not None:
            try:
                result = self.database.animals.insert_one(data)
                return result.acknowledged
            except Exception:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    # Read method to implement the R in CRUD.
    # data: Identifies the document(s) to be read (Must be a dictionary)
    # Returns cursor if read is successful or message if no document was found
    # Raises exception if data is None
    def read(self, data):
        if data is not None:
            # If/Else statement checks if at least one document is found
            if self.database.animals.count_documents(data, limit = 1) != 0:
                result = self.database.animals.find(data)
            else:
                result = "No document was found"
            return result
        else:
            raise Exception("Nothing to find, because data parameter is empty")
            
    # Update method to implement the U in CRUD.
    # Method takes two arguments find_filter and data
    # find_filter: Identifies the document(s) to be updated
    # data: Fields and values to be updated (Must be a dictionary)
    # Returns dictionary/JSON if update is successful or message if no document was found
    # Raises exception if data is None
    def update(self, find_filter, data):
        if data is not None:
            # If/Else statement checks if at least one document is found
            if self.database.animals.count_documents(find_filter, limit = 1) != 0:
                update_result = self.database.animals.update_many(find_filter, {"$set": data})
                result = update_result.raw_result
            else:
                result = "No document was found"
            return result
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            
    # Delete method to implement the D in CRUD.
    # data: Identifies document(s) to be deleted (Must be a dictionary)
    # Returns dictionary/JSON if delete is successful or message if no document was found
    # Raises exception if data is None
    def delete(self, data):
        if data is not None:
            # If/Else statement checks if at least one document is found
            if self.database.animals.count_documents(data, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(data)
                result = delete_result.raw_result
            else:
                result = "No document was found"
            return result
        else:
            raise Exception("Nothing to delete, because data parameter is empty")