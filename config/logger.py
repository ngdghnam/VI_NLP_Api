import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler
import json
from datetime import datetime

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        # Create a dictionary with log record information
        log_obj = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
        }
        
        # Add exception info if present
        if record.exc_info:
            log_obj["exception"] = self.formatException(record.exc_info)
            
        return json.dumps(log_obj)

def get_logger(name: str = "fastapi_app") -> logging.Logger:
    # Create logs directory
    log_dir = Path(__file__).parent.parent / "logs"
    log_dir.mkdir(exist_ok=True)

    # Configure logging
    logger = logging.getLogger(name)
    
    # Only add handlers if they haven't been added already
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Console handler with colored output
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_formatter = logging.Formatter(
            '%(levelname)s: %(message)s',
        )
        console_handler.setFormatter(console_formatter)

        # File handlers
        file_formatter = JsonFormatter()

        # Error log file handler
        error_handler = RotatingFileHandler(
            log_dir / "error.log",
            maxBytes=10485760,  # 10MB
            backupCount=5,
        )
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(file_formatter)

        # Combined log file handler
        combined_handler = RotatingFileHandler(
            log_dir / "combined.log",
            maxBytes=10485760,  # 10MB
            backupCount=5,
        )
        combined_handler.setLevel(logging.INFO)
        combined_handler.setFormatter(file_formatter)

        # Exception log file handler
        exception_handler = RotatingFileHandler(
            log_dir / "exceptions.log",
            maxBytes=10485760,  # 10MB
            backupCount=5,
        )
        exception_handler.setLevel(logging.ERROR)
        exception_handler.setFormatter(file_formatter)

        # Add all handlers to logger
        logger.addHandler(console_handler)
        logger.addHandler(error_handler)
        logger.addHandler(combined_handler)
        logger.addHandler(exception_handler)

        # Remove console handler in production
        # if os.getenv("ENV") == "production":
        #     logger.removeHandler(console_handler)

    return logger

# Create a default logger instance
logger = get_logger()