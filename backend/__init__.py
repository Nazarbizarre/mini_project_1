from os import getenv

from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter
import atexit

from .routes import article_router, auth_router, admin_router


from .logging.loggers import log_program_start, log_program_stop

app = FastAPI()

log_program_start()
atexit.register(log_program_stop)


api_router = APIRouter(prefix="/api")
api_router.include_router(article_router)
api_router.include_router(auth_router)
api_router.include_router(admin_router)
app.include_router(api_router)
