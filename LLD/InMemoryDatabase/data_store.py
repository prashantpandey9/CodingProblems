# Implement a data store using a combination of hash maps and custom data structures.
import time


class DataStore:
    def __init__(self):
        self.store = {}
        self.expiry_time = {}
    
    def set(self, key, value, ttl=None):
        self.store[key] = value
        if ttl:
            self.expiry_time[key] = time.time() + ttl
    
    def get(self, key):
        """
        Retrieve a value by key. Check for expiration.
        """
        if key in self.expiry_time and time.time() > self.expiry_time.get(key):
            self.delete(key)
            return None
        
        return self.store.get(key)

    
    def delete(self, key):
        """
        Remove key-value pair
        """
        if key in self.store:
            del self.store[key]
        else:
            raise ValueError
        
        if key in self.expiry_time:
            del self.expiry_time
    
    def keys(self):
        """
        Return all keys in the store.
        """
        return list(self.store.keys())