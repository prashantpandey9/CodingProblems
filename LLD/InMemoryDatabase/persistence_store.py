import json

class Persistencemanaged:
    @staticmethod
    def save_to_disk(store, file_path):
        with open(file_path, 'w') as file:
            json.dump(store, file)
    
    @staticmethod
    def load_from_disk(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    