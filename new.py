# x = 2*729**333+2*243**334-81**335+2*27**336-2*9**337-338
# k = 0
# количество не нулевых чисел в записи числа в 9 cntgtyb
# while x > 0:
#     if x % 9 != 0:
#         k+=1
#     x = x // 9

# print(k)

#
# x = 3*2187**2020+3*729**2021-2*81**2022+27**2023-4*3**2024-2029
# k = 0
# while x > 0:
#     if x % 27 > 9:
#         k += 1
#     x = x // 27

# print(k)

# x = 4*3125**2019+3*625**2020-2*125**2021+25**2022-4*5**2023-2024
# k = 0
# while x > 0:

#     if x % 25 > 10:
#         k+= 1
#     x = x // 25
# print(k)

# x = 2*729**2014+2*243**2016-2*81**2018+2*27**2020-2*9**2022-2024

# k = 0
# while x > 0:
#     if x % 27 > 9:
#         k+= 1
#     x = x // 27

# print(k)

# x = 4**644+4**322+16**35-64**3
# k = 0
# while x > 0:
#     if x % 4 == 3:
#         k += 1
#     x = x // 4

# print(k)

# for i in range(8):
#     x = 7*8**2+2*8+3
#     a = 11*16**3+1*16**2+3*16+10
#     c = 1*2**10+1*2**7+1*2**6+1*2**5+1*2**4+1*2

#     if 

# a = int('723', 8)
# b = int('B13A', 16)
# c = int('10011101010', 2)
# x = a * b - c
# k = 0
# while x > 0:
#     if x % 4 == 0:
#         k += 1
#     x = x // 4
# print(k)
# в 9 систему
# x = 100
# s = ''
# while x > 0:
#     s = str(x % 9) + s
#     x = x // 9
# print(s)
# 
# for x in range(2, 31):
#     n = 31
#     if n % x == 4:
#         print(x)

# for q in range(3, 23):
#     n = 23
#     if x == int('212', q)
#     s = ''
#     while n > 0:
#         s = str(n % q) + s
#         n = n // q
#     if s == '212':
#         print(q)
#         break


# восмеричное число 77 в некоторой системе счисления записывается как 53
# n = int('77', 8) # из любой в 10
# for i in range(6, 36):
#     if n == int('53', i):
#         print(i)
#         break

# в системе счисления с основанием n запись числа 144 оканчивается на 1 и не менее 3 чисел
# 2 потому что оканчивается на 1
# for n in range(2, 36):
#     s = ''
#     x = 144
#     while x > 0:
#         s = str(x % n) + s
#         x = x // n
    
#     if len(s) > 2 and s[-1] == '1' and int(s, n) == 144:
#         print(n)
        
    
# for i in range(4, 36):
#     n = int('12', i) * int('13', i)
#     c = int('211', i)
#     if n == c:
#         print(i)
#         break

# for i in range(4, 36):
#     c = int('101', i) + 13
#     b = int('101', i + 1)
#     if c == b:
#         print(i)

# for i in range(3, 36):
#     c = int('121', i) + 1
#     b = int('101', 7)
#     if c == b:
#         s = ''
#         while i > 0:
#             s = str(i % 3) + s
#             i = i // 3
  
#         print(s)

# for i in range(7, 36):
#     n = int('12', i) * int('33', i)
#     c = int('406', i)
#     if n ==c:
#         print(i)


#               САМОСТОЯТЕЛЬНАЯ 10.10  ||  ЗАДАНИЕ 14.1
# 1
for x in range(0, 100):
    a = int('35', 6)
    b = int('35', 7)
    if a + x== b:
        print(x)
        break

# 2
x = 27
s = ''
while x > 0:
    s = str(x % 4) + s
    x = x // 4
print(s)


# 3
for i in range(4, 36):
    x = 23
    s = ''

    while x > 0:
        s = str(x % i) + s
        x = x // i

    if s[-1] == '2':
        print(i)


# 4
for i in range(4, 36):
    x = int('65', 8)

    if x == int('311', i):
        print(i)


# 5
for i in range(2, 36):
    a = int('101', i + 1)
    b = int('101', i) + int('11', 16)
    if a == b:
        print(i)

# 6
for i in range(8, 36):
    x = int('77', 8)

    if x == int('70', i):
        print(i)

# 7
for n in range(2, 36):
    s = ''
    x = 93
    while x > 0:
        s = str(x % n) + s
        x = x // n
    
    if len(s) > 2 and s[-1] == '2' and int(s, n) == 93:
        print(n)
        
    
# 8
for i in range(4, 36):
    a = int('12', i) * int('13', i)
    b = int('222', i)
    if a == b:
        print(i)


# 9
for i in range(5, 36):
    a = int('13', i) * int('31', i)
    b = int('423', i)
    if a == b:
        print(i)

# 10
for i in range(4, 36):
    a = int('103', i) + 11
    b = int('103', i + 1)
    if a == b:
        print(i)