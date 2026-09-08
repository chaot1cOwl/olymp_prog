from utility.simple_logger import log_function

n = 3
@log_function
def search(k, subset, _log_depth=1):
    if k == n+1:
        print(subset)
    else:
        subset.append(k)
        search(k+1, subset, _log_depth=_log_depth+1)
        del subset[-1]
        search(k+1, subset, _log_depth=_log_depth+1)

search(1, [])
