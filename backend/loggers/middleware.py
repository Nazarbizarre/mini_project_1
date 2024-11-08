from fastapi import Request, Depends
from .loggers import requests_logger
from datetime import datetime

async def log_request(request: Request):
    request_time = datetime.now()

    headers = dict(request.headers)
    body = await request.json() if request.method in ["POST", "PUT", "PATCH", "GET"] else None
    requests_logger.info(
        f"Request Time: {request_time}, Handler: {request.url.path}, Method: {request.method}, "
        f"Headers: {headers}, Body: {body}, User-Agent: {headers.get('user-agent')}"
    )

async def request_logging_dependency(request: Request):
    await log_request(request)