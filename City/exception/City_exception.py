from City.logging.loggers import setup_log_config
import os
import sys
from datetime import datetime
import traceback
import logging

class CityscapeException(Exception):
    def __init__(self, error_message, error_info: sys):
        super().__init__(error_message)  
        self.error_message = error_message
        exc_type, exc_value, exc_traceback = error_info.exc_info()
        
        logger = logging.getLogger('sam_logger')
        logger.error(f"Exception Type: {exc_type}")
        logger.error(f"Exception Value: {exc_value}")
        logger.error(f"Traceback:\n{''.join(traceback.format_tb(exc_traceback))}")
        logger.error(f"Error Message: {self.error_message}")
    
    def __str__(self):
        return f"CityscapeException: {self.error_message}"

if __name__ == '__main__':
    setup_log_config()  
    logger = logging.getLogger('sam_logger')
    
    try:
        logger.info("Entering the try block")
        a = 1 / 0  
    except Exception as e:
        raise CityscapeException(e, sys)




        
        