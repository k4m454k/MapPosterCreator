import logging


def log_processing(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info(f"Processing {func.__name__}...")
        value = func(*args, **kwargs)
        return value

    return wrapper