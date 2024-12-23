import os
from datetime import datetime

def log_file_create():
    current_dir = os.getcwd()
    
    LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.txt"
    
    logs_dir = os.path.join(current_dir, "logs",LOG_FILE_NAME )
    
    os.makedirs(logs_dir, exist_ok=True)
    
    full_log_path = os.path.join(logs_dir, LOG_FILE_NAME)
    
    print(f"Log file created at: {full_log_path}")
    return full_log_path