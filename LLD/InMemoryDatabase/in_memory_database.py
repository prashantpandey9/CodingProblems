from data_store import DataStore
from query_processor import QueryProcessor
from concurrency_manager import ConcurrencyManager

class InMemoryDatabase:
    def __init__(self):
        self.data_store = DataStore()
        self.query_processor = QueryProcessor()
        self.concurrency_manager = ConcurrencyManager()
    
    @ConcurrencyManager.synchronized
    def set(self, key, value, ttl=None):
        self.data_store.set(key, value, ttl)
    
    @ConcurrencyManager.synchronized
    def get(self, key):
        return self.data_store.get(key)
    
    @ConcurrencyManager.synchronized
    def delete(self, key):
        self.data_store.delete(key)
    
    @ConcurrencyManager.synchronized
    def query(self, condition):
        return self.query_processor.filter_by_value(self.data_store.store, condition)