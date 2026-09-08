from utility.simple_logger import log_function

@log_function
def factorial(n, _log_depth=1):
    if n <= 1:
        return 1
    return n * factorial(n - 1, _log_depth=_log_depth + 1)

factorial(4)
