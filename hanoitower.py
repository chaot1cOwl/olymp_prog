from utility.simple_logger import log_function

@log_function
def hanoi_towers(n, from_peg, to_peg, _log_depth=1):
    if n == 1:
        print(f"Переместить диск со стержня {from_peg} на стержень {to_peg}")
        return
    unused_peg = 6 - from_peg - to_peg
    hanoi_towers(n-1, from_peg, unused_peg, _log_depth=_log_depth+1)
    print(f"Переместить диск со стержня {from_peg} на стержень {to_peg}")
    hanoi_towers(n-1, unused_peg, to_peg, _log_depth=_log_depth+1)



disc_count = 5

hanoi_towers(disc_count, 1, 3)
