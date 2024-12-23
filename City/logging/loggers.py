import logging
import os
import sys
import logging.config
from City.utils.main_func import log_file_create


def setup_log_config():
    '''Setting up logging configuration'''
    log_config={
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console_format':{
                'format': '%(name)s - %(levelname)s - %(message)s',
            },
            'file_format': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': "INFO",
                'formatter':'console_format',
            },
            'file': {
                'class': 'logging.FileHandler',
                'level': "INFO",
                'formatter':'file_format',
                'filename': log_file_create(),
            },
        },
        'loggers': {
            'sam_logger': {  # Logger for any files that i want log of
                'handlers': ['console','file'],
                'level': 'INFO',
                'propagate': False,
            },
        },
    }
    logging.config.dictConfig(log_config)
