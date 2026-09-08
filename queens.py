from utility.simple_logger import log_function




n = 8
count = 0
col, diag1, diag2 = [0]*n, [0]*n*2, [0]*n*2
@log_function
def search(y, _log_depth=1):
    if y == n:
        global count
        count += 1
        return
    for x in range(n):
        if col[x] or diag1[x+y] or diag2[x-y+n-1]: continue
        col[x] = diag1[x+y] = diag2[x-y+n-1] = 1
        search(y+1, _log_depth=_log_depth+1)
        col[x] = diag1[x+y] = diag2[x-y+n-1] = 0


search(0)
print(count)