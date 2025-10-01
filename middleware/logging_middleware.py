from datetime import datetime
import time  # Import the time module directly
from starlette.middleware.base import BaseHTTPMiddleware
from config.logger import logger

from fastapi import Request
from fastapi import FastAPI

# Logger middleware
class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Get request details
        start_time = time.time() 
        method = request.method
        url = request.url.path
        query_params = str(request.query_params)
        client_host = request.client.host if request.client else "unknown"
        
        # Process the request
        try:
            response = await call_next(request)
            
            # Calculate processing time
            process_time = time.time() - start_time
            
            # Format log
            log_message = (
                f'{client_host} - - [{datetime.now().strftime("%d/%b/%Y:%H:%M:%S %z")}] '
                f'"{method} {url}{query_params if query_params != "" else ""} HTTP/{request.scope.get("http_version", "1.1")}" '
                f'{response.status_code} - '
                f'{process_time:.4f}s'
            )
            
            # Log at appropriate level based on status code
            if 400 <= response.status_code < 500:
                logger.warning(log_message)
            elif response.status_code >= 500:
                logger.error(log_message)
            else:
                logger.info(log_message)
                
            return response
        
        except Exception as e:
            process_time = time.time() - start_time
            logger.error(
                f'{client_host} - - [{datetime.now().strftime("%d/%b/%Y:%H:%M:%S %z")}] '
                f'"{method} {url} HTTP/{request.scope.get("http_version", "1.1")}" '
                f'500 - {process_time:.4f}s - Exception: {str(e)}',
                exc_info=e
            )
            raise

def add(app: FastAPI):
    app.add_middleware(RequestLoggingMiddleware)