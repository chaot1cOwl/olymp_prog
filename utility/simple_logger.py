import sys
import functools
from loguru import logger

logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | {level} | {message}"
)


def log_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        depth = kwargs.get("_log_depth", 1)
        logger.opt(depth=depth).debug(f"{"-"*+depth} Entering {func.__name__} with args: {args}, kwargs: {kwargs}")
        if "_log_depth" in kwargs:
            kwargs["_log_depth"] = depth + 1
        result = func(*args, **kwargs)
        logger.opt(depth=depth).debug(f"{"-"*+depth} Exiting {func.__name__} with result: {result}")
        return result
    return wrapper