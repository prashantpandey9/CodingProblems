import threading

class ConcurrencyManager:
    lock = threading.Lock()
    
    @classmethod
    def synchronized(cls, func):
        def wrapper(*args, **kwargs):
            with cls.lock:
                return func(*args, **kwargs)
        return wrapper
