# 10進数 -> base進数に変換
def base10to(x: int, base: int) -> str:
    s = ''

    while x > 0:
        s = str(x % base) + s
        x = x // base

    return s