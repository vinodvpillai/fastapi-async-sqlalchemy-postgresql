import logging
import sys
from app.core.env_settings import settings

# Logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Log format
fmt = logging.Formatter(
    "%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(process)d >>> %(message)s"
)

# Create handlers - Standard output & File
stdoutHandler = logging.StreamHandler(stream=sys.stdout)
msgHandler = logging.FileHandler("msg.log")

# Set the log format on each handler
stdoutHandler.setFormatter(fmt)
msgHandler.setFormatter(fmt)

# Set the log levels on the handlers
stdoutHandler.setLevel(settings.CONSOLE_LOG_INFO_LEVEL)
msgHandler.setLevel(settings.FILE_LOG_INFO_LEVEL)

# Add each handler to the Logger object
logger.handlers = [stdoutHandler, msgHandler]