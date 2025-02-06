# def f(n):
#     if n == 1: return 3

#     if n > 1: return f(n - 1) * (n - 1)
# print(2345)

# def f(n):
#     if n == 1: return 1
#     if n > 1: return f(n - 1) * f(n - 1) - f(n - 1) * n + 2 * n
# print(f(4))
#  ANS = 20


#  ANS = 134

# def g(n):
#     if n == 1: return 1
#     if n > 1: return g(n - 1) * n

# def f(n):
#     if n == 1: return 0
#     if n  >1: return f(n - 1) + n

# print(f(5) + g(5))

# ANS = 4095
# def f(n):
#     if n == 1: return 1
#     if n > 1: return f(n - 1) + 2 ** (n - 1)
# print(f(12))

# import sys
# sys.setrecursionlimit(10000)

# def f(n):
#     if n == 1: return 1
#     if n > 1: return n * f(n - 1)
# print(f(2023) / f(2020))


# import sys
# sys.setrecursionlimit(10000)

# def f(n):
#     if n == 1: return 1
#     if n > 1: return n * f(n - 1)
# print((2 * f(2024) + f(2023)) / f(2022))

# import sys
# sys.setrecursionlimit(10000)

# from functools import lru_cache
# @lru_cache(None)

# def f(n):
#     if n <= 3: return n
#     if n > 3 and n % 2 == 0: return f(n - 1) + 2 * f(n // 2)
#     if n > 3 and n % 2 != 0: return f(n - 1) + f(n - 3)

# k = 0
# for n in range(1, 1000):
#     res = f(n)
#     if res < 10 ** 8:
#         print(res)
#         k += 1

from functools import lru_cache
@lru_cache(None)

def f(n):
    if n > 20: return n * n * n + n
    if n <= 20 and n % 2 == 0: return 3 * f(n + 1) + f(n + 3)
    if n <= 20 and n % 2 != 0: return f(n + 2) + 2 * f(n + 3)
k = 0

for n in range(1, 1001):
    if str(f(n)).count('1') == 0:
        k += 1
print(k)