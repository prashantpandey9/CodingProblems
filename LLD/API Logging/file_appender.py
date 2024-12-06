from log_appender import LogAppender

class FileAppender(LogAppender):
    def appender(self, log_message):
        with open("log.txt", "a") as file:
            file.write(str(log_message) + "\n")
        