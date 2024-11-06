from uvicorn import run

from backend import app
from backend.db import AsyncDB


if __name__ == "__main__":
    AsyncDB.migrate()
    run("run_backend:app")
