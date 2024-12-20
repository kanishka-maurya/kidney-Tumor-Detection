import os
import sys
from logging import *



logging_str = "%(asctime)s: %(levelname)s: %(module)s: %(message)s"

log_dir = "logs"
os.makedirs(log_dir,exist_ok=True)
log_filepath = os.path.join(log_dir,"running_logs.log")

# this will log message to running_logs.log file in logs folder
basicConfig(
        level = INFO,
        format = logging_str,

        handlers = [
            FileHandler(log_filepath),
            StreamHandler(sys.stdout)
        ]



)

# creating a logger object named cnnClassifierLogger which can be used in other files for logging messages
logger = getLogger("cnnClassifierLogger")