import logging
import sys
from typing import List

from core.logging import InterceptHandler
from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

config = Config(".env")

VERSION = "0.1.0"
DEBUG: bool = config("DEBUG", cast=bool, default=False)
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret, default="")

APP_NAME: str = config("APP_NAME", default="FastAPI")
API_PREFIX: str = config("API_PREFIX", default="")
LISTEN_PORT: int = config("LISTEN_PORT", default=5000)
BIND: str = config("BIND", default="127.0.0.1")
WORKERS: int = config("WORKERS", default=1)

# logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
