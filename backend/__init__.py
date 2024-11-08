from os import getenv

from dotenv import load_dotenv
from fastapi import (FastAPI,
                     APIRouter)
from contextlib import asynccontextmanager
import signal
import asyncio

from .routes import (article_router,
                     auth_router,
                     admin_router)
from .loggers.loggers import (
                            log_program_start,
                            log_program_stop) 


shutdown_reason = None

def signal_handler(sig, frame):
    global shutdown_reason
    if sig == signal.SIGINT:
        shutdown_reason = "Interrupted by User"
    elif sig == signal.SIGTERM:
        shutdown_reason = "Terminated by Server"
    log_program_stop(reason=shutdown_reason)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

@asynccontextmanager
async def lifespan(app: FastAPI):
    log_program_start()
    yield

app = FastAPI(lifespan=lifespan)



api_router = APIRouter(prefix="/api")
api_router.include_router(article_router)
api_router.include_router(auth_router)
api_router.include_router(admin_router)
app.include_router(api_router)
