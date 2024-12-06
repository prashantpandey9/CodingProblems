from log_appender import LogAppender

class ConsoleAppender(LogAppender):
    def appender(self, log_message):
        print(log_message)