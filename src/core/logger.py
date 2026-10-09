import os

from loguru import logger

from core.config import settings


def setup_logging() -> None:
    logger.add(
        os.path.join(settings().BASE_DIR.parent, 'logs/errors/log_{time}.log'),
        level='ERROR',
        format='{time} {message}',
        rotation='1 day',
    )
    logger.add(
        os.path.join(settings().BASE_DIR.parent, 'logs/info/log_{time}.log'),
        level='INFO',
        format='{time} {level} {message}',
        rotation='1 day',
    )
