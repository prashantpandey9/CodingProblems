from logger import Logger
from logger_config import LoggerConfig
from log_level import LogLevel
from file_appender import FileAppender


class LoggerFrameWorkDemo:
    @staticmethod
    def run():
        logger = Logger.get_instance()
        
        # Logging with default configuration
        logger.info("This is information message")
        logger.warning("This is Warning message")
        logger.error("This is an error message")
        
        # changing 
        config = LoggerConfig(LogLevel.DEBUG, FileAppender())
        logger.set_config(config)
        
        logger.debug("This is a debug log")
        logger.info("This is a Info log")


if __name__ == "__main__":
    LoggerFrameWorkDemo.run()