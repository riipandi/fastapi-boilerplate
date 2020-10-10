import pathlib

import uvicorn
from core.config import (API_PREFIX, APP_NAME, BIND, DEBUG, LISTEN_PORT,
                         VERSION, WORKERS)
from core.events import create_start_app_handler
from core.routes import router as api_router
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Root project directory
rootdir = pathlib.Path().absolute()

def get_application() -> FastAPI:
    application = FastAPI(title=APP_NAME, debug=DEBUG, version=VERSION)
    application.include_router(api_router, prefix=API_PREFIX)
    application.mount("/static", StaticFiles(directory=f"{rootdir}/app/static"), name="static")
    pre_load = False
    if pre_load:
        application.add_event_handler("startup", create_start_app_handler(application))
    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app", host=BIND, port=int(LISTEN_PORT), reload=DEBUG, debug=DEBUG, workers=int(WORKERS))
