from abc import ABC, abstractmethod

class LogAppender(ABC):
    @abstractmethod
    def appender(self, log_message):
        pass