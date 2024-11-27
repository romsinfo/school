# 2:   -- со второго числа
# n = 26
# r = bin(n)
# r = r[2:]

# r = r[::-1] 

# for i in range(2, 1000):
#     r = bin(i)[2:]

#     if r.count('1') % 2 == 0:
#         r += '00'
#     else:
#         r += '10'

#     r = int(r, 2) #  в 10 систему
#     if r > 125:
#         print(i)
#         break



# c = [] # МИНИМАЛЬНОЕ ЧИСЛО
# for n in range(2, 1000):
#     r = bin(n)[2:]

#     if n % 2 == 0:
#         r += '10' + r
#     else:
#         r += '10' + r + '01'

#     r = int(r, 2) #  в 10 систему
#     if n <= 12:
#         c.append(r)

# print(max(c))

# s = '10110110011'
# s2 = ''
# s = s.replace('1', '2').replace('0', '1').replace('2', '0') # 01001001100
# print(s)


# for n in range(10000, 100000):
#     r = str(n)
#     x1=int(r[0]) + int(r[2]) + int(r[4])
#     x2=int(r[1]) + int(r[3])

#     if x1 > x2:
#         r = str(x2) + str(x1)
#     else:
#         r = str(x1) + str(x2)
    
#     if r == '621':
#         print(n)
#         break


#  наибольшее возможное двухзначное и наименьшее
# k = 0
# for n in range(900, 1000):
#     g = sorted(str(n))

#     x1 = int(g[2] + g[1])
#     x2 = int(g[0] + g[1])

#     if 10 <= x1 < 100 and 10 <= x2 < 100 and (x1 - x2) == 70:
#         k += 1
# print(k)


# newSet = set()

# for n in range(1, 1000):  # СТАВИМ 1, НЕ 0 ПОТОМУ ЧТО НАТУРАЛЬНОЕ ЧИСЛО
#     r = bin(n)[2:] #  в двоичную

#     r = r + str(r.count('1') % 2)
#     r = r + str(r.count('1') % 2)

#     r = int(r, 2)

#     if r < 100:
#         newSet.add(r)
    
# print(len(newSet))

# for n in range(1, 1000):

#  ВОСЬМИБИТНЫЙ ВИД ----
# n = 26
# r = bin(n)[2:]
# print(r)

# r = (8 - len(r)) * '0' + r  #  ВОСЬМИБИТНЫЙ ВИД
# print(r)
#  ----

# for n in range(256):
#     r = (8 - len(str(n)))


# n = 90
# r = bin(n)[2:]
# r = (8 - len(r)) * '0' + r  #  ВОСЬМИБИТНЫЙ ВИД
# print(r)
# i = r[::-1]
# i1 = ''
# k = 0
# for x in range(len(i) - 1):
#     if i[x] == '1' and k == 0:
#         i = i[x:]
#         k += 1

# print(i[::-1])


#  4
# for x1 in 0, 1:
#     for x2 in 0, 1:
#         for x3 in 0, 1:
#             for x4 in 0, 1:
#                 print(x1, x2, x3,x4) 



# mx = 0 
# c = []
# for n in range(1, 1000):
#     r = bin(n)[2:]

#     if n % 2 == 0:
#         r = r + r[-2:]
#     else:
#         r = '1' + r + '0'

#     r = int(r, 2)

#     if r < 100:
        
#         c.append(n)

# print(max(c))


# mx = 0
# for n in range(4, 100):
#     s = '3' + n * '5'
#     while '333' in s or '555' in s:
#         if '555' in s:
#             s=s.replace('555', '3', 1)
#         else:
#             s=s.replace('333', '5', 1)
    
#     res = s.count('3') * 3 + s.count('5') * 5
#     if res > mx:
#         mx = res

# print(mx)  # 12 задание


# x = 2 * 729 ** 333 + 2 * 243 ** 334 - 81 ** 335 + 2 * 27 ** 336 - 2 * 9 ** 337 - 338
# c = 0
# while x > 0:
#     if x % 9 != 0:
#         c+=1
#     x = x // 9
# print(c)


###  №10



# s = '012345678'
# s1 = '12345678'
# n = 0
# for x1 in s:
#     for x2 in s:
#         for x3 in s:
#             for x4 in s:
#                 for x5 in s:
#                     w = x1 + x2 + x3 +x4 + x5
#                     if w.count('5') == 1 and x1 != x2 != x3

# arr = []
# for n in range(1000):
#     r = bin(n)[2:]
#     if r.count('1') % 2 == 0:
#         r = '10' + r[2:] + '0'
#     else:
#         r = '11' + r[2:] + '1'  # первые 2 разряда 
#     r = int(r, 2)

#     if r < 35:
#         arr.append(n)

# print(max(arr))

# maxi = 0
# arr = []
# def toFifth(n):
#     s = ''
#     while n > 0:
#         s = str(n % 5) + s
       
#         n = n // 5

#     return s

# for x in range(2025, 1000, -1):
#     n = 5 ** 2025 + 5 ** 200 - x
#     r = toFifth(n)

#     if r.count('4') > maxi:
#         maxi = r.count('4')
#         arr.append(x)

# print(maxi)
# print(arr[-1])


# def toFifth(n, G):
#     s = ''
#     while n > 0:
#         s = str(n % G) + s
       
#         n = n // G

#     return s

# for p in range(8, 10000):
#     for x in range(p):
#         for y in range(p):
#             c = (x * y) ** 2
#             r = toFifth(c, p)
            
#             if 45 * 67 == int(r):
#                 print(r)
#                 print(c)


# class MyClass:
#     def greeting():
#         print('Hello')

# a = MyClass.greeting()
from ast import Break
from unittest.util import sorted_list_difference


n = 0

# for x1 in 'АГМНСТУ':
#     for x2 in 'АГМНСТУ':
#         for x3 in 'АГМНСТУ':
#             for x4 in 'АГМНСТУ':
#                 for x5 in 'АГМНСТУ':
#                     for x6 in 'АГМНСТУ':
#                         w = x1+x2+x3+x4+x5+x5
#                         n+=1
                       
                    
# s = '0123456789ABCDEF'
# s1 = '123456789ABCDEF'
# sc = '02468ACE'
# snc = '13579BDF'
# n = 0
# for x1 in sc:
#     for x2 in snc:
#         for x3 in sc:
#             w = x1+x2+x3

#             if len(set(w)) == 3 and x1 != '0':
#                 n += 1
# print(n)



# s = 'АЕКРТ'

# n = 0
# a = []
# for x1 in s:
#     for x2 in s:
#         for x3 in s:
#             for x4 in s:
#                 for x5 in s:
#                     for x6 in s:
#                         w = x1+x2+x3+x4+x5+x6
#                         n += 1
#                         if w == 'КАРЕТА' or w == 'РАКЕТА':
#                             a.append(n)


# print(max(a) - min(a) - 1)


# s = '0123456789ab'
# sk3 = '0369'
# snk3 = '124578ab'
# k = 0
# ##  ЧЕРЕДУЕМ SN И SNK 
# for x1 in sk3:
#     for x2 in snk3:
#         for x3 in sk3:
#             for x4 in snk3:
#                 for x5 in sk3:
#                     for x6 in snk3:
#                         for x7 in sk3:
#                             w = x1+x2+x3+x4+x5+x6+x7
#                             if x1 != '0':
#                                 k += 1
# for x1 in snk3:
#     for x2 in sk3:
#         for x3 in snk3:
#             for x4 in sk3:
#                 for x5 in snk3:
#                     for x6 in sk3:
#                         for x7 in snk3:
#                             w = x1+x2+x3+x4+x5+x6+x7
#                             if x1 != '0':
#                                 k += 1


# print(k)



# class MyClass():
#     def printMy(*args):
#         print(args)

# MyClass.printMy(1, 2, 'hello')



#   8 PYTHON 
# s = 'КУСАТЬ'
# s1 = 'КУСАТ'
# n = 0
# for x1 in s1:
#     for x2 in s:
#         for x3 in s:
#             for x4 in s:
#                 for x5 in s:
#                     w = x1+x2+x3+x4+x5
#                     if w.count('СУК') == 0 and len(set(w)) == 5:
#                         n+=1
# print(n)

# s = 123
# # n = sum(map(int, s))
# g = 0
# for i in str(s):
#     g += int(i)
# # print(n) #  СУММА ВСЕХ ЦИФР
# print(g) #  СУММА ВСЕХ ЦИФР










# print('x, y, z, w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (w <= y) and ((x <= z) ==(y <= x))
#                 if f:
#                     print(x, y, z, w)

# arr = []
# for A in range(1, 10000):
#     k = 0
#     for x in range(0, 10000):
#         f = (((x & 13 != 0) or (x & 39 == 0)) <= (x & 13 != 0)) or ((x & A == 0) and (x & 13 == 0))
#         if f == False:
#             k += 1
#             break
#     if k== 0:
#         arr.append(A)
# print(max(arr))


# arr = []
# for A in range(1, 10000):
#     k = 0
#     for x in range(0, 10000):
#         f = (x & 49 != 0) <= ((x & 33 == 0) <= (x & A != 0))
#         if f == False:
#             k += 1
#             break
#     if k== 0:
#         print(A)
#         break





# arr = []
# for A in range(1, 10000):
#     k = 0
#     for x in range(0, 10000):
#         f = (((x & 13 != 0) or (x & A != 0)) <= (x & 13 != 0)) or ((x & A != 0) and (x & 39 == 0))
#         if f == False:
#             k += 1
#             break
#     if k== 0:
#         arr.append(A)
# print(max(arr))



# arr = []
# for A in range(1, 10000):
#     k = 0
#     for x in range(0, 10000):
#         f = ((x | 42 > 64) and (x | 34 <= 102)) <= (not(x | A < 70))
#         if f == False:
#             k += 1
#             break
#     if k== 0:
#         print(A)
#         break









# a = set(i for i in range(1, 51))             
# p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
# q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}

# for x in range(1, 51):
#     f = ((x in a) <= (x in p)) or (not(x in q) <= (not(x in a)))
#     if f == 0:
#         a.remove(x)
# print(len(a))



# a = set()             
# p = {1, 12}
# q = {12, 13, 14, 15, 16}

# for x in range(1, 51):
#     f = not(x in a) <= (not(x in p) and not(x in q))
#     if f == 0:
#         a.add(x)
# print(a)


# for x in [k * 0.25 for k in range(-100000, 100000)]:
#     a = 1 #  a  - наибольшее
#     p = 10<= x<=14
#     q = 5<=x<=20
#     r = 15<=x<=25
#     f1 = (not a) <= p
#     f2 = q <= r
#     if f1 != f2: print(x)  #  15 - 5


# for x in [k * 0.25 for k in range(-100000, 100000)]:
#     a = 0 #  a  - НАИМЕНЬШЕЕ
#     p = 4<= x<=15
#     q = 12<=x<=20
#     r = 15<=x<=25
#     f1 = (p and q) <= a  # было - ((x in p) and (x in q) <= (x in a))
 
#     if f1 == 0: print(x)  #  15 - 5


# for x in [k * 0.25 for k in range(-100000, 100000)]:
#     a = 0 #  a  - НАИМЕНЬШЕЕ
#     b = 23<=x<=37
#     c = 41 <= x <= 73
#     f1 = (not((not(b) <= c)) <= a)
 
#     if f1 == 1: print(x)  #  15 - 5

# s = []
# for x in [k * 0.25 for k in range(-1000000, 1000000)]:
#     a = 0 #  a  - НАИМЕНЬШЕЕ
#     p = 1023<=x<=2148
#     q = 1362<=x<=3898
#     r = 1813<=x<=2566
#     f1 = ((not((x) <= ((p) or (r)))) <= (not(a) <= (not(q))))
 
#     if f1 == 0: 
#         s.append(x)

# print(max(s) - min(s))

# arr = []
# for x in [k * 0.25 for k in range(-1000000, 1000000)]:
#     a = 0
#     p = 37<=x<=60
#     q = 40<=x<=77
#     f = p <= ((q and a) <= p)
#     if f == 0:
#         arr.append(x)
# print(max(arr) - min(arr))



# arr = []
# for x in [k * 0.25 for k in range(-1000000, 1000000)]:
#     a = 0
#     p = 5<=x<=110
#     q = 15<=x<=42
#     r = 25<=x<=70
#     f = p <= q or (not(a) <= (not(r)))
#     if f == 0:
#         arr.append(x)
# print(max(arr) - min(arr))

# arr = []
# for x in [k * 0.25 for k in range(-1000000, 1000000)]:
#     a = 0
#     p = 14<=x<=34
#     q = 24<=x<=44
#     f = a <= q == p
#     if f == 0:
#         arr.append(x)
# print(max(arr) - min(arr))

# # 30

# arr = []
# for x in [k * 0.25 for k in range(-100000, 100000)]:
#     a = 1
#     p = 10<=x<25
#     q = 15<=x<=30
#     r = 25<=x<=40
#     f = (q <= (not(r))) and a and not(p)
#     if f == 0:
#         arr.append(x)
# print(max(arr) - min(arr))
# arr = []
# for x in [k * 0.25 for k in range(-1000000, 1000000)]:
#     a = 0
#     p = 1381<=x<2165
#     q = 369<=x<=3894
#     r = 2543<=x<=3155
#     f = (not(q) <= (p or r) <= (not(a) <= (not(q)))
#     if f == 0:
#         arr.append(x)
# print(max(arr) - min(arr))

# import sys
# sys.setrecursionlimit(10000)

# def f(x, y):
#     if x < y: return 0
#     if x == y: return 1
#     if x > y: return f(x -2 , y) + f(x // 2, y)
# print(f(32, 8) * f(8, 1))

# def f(x, y):
#     if x < y: return 0
#     if x == 13: return 0
#     if x == y: return 1
#     if x > y: return f(x + 2, y) + f(x*3, y) + f(x**2, y)
# print(f(3, 49))

# def f(x,  y):
#     if x > y: return 0
#     if x == y: return 1
#     if x < y: return f(x + 1, y) + f(x * 4, y)
# print(f(1, 32))

# def f(x, y):
#     if x == 25: return 0
#     if x == y: return 1
    
#     if x > y: return 0
#     if x < y: return f(x + 1, y) + f(2 * x + 1, y)
# print(f(1, 31))

# def f(x, y):
#     if x == y: return 1
#     if x == 15: return 0
#     if x > y: return 0
#     if x < y: return f(x + 1, y) + f(x + 2, y)
# print(f(3, 9) * f(9, 20))


# def f(x, y):
#     if x == 10: return 0
#     if x > y: return 0
#     if x == y: return 1
#     if x < y: return f(x + 1, y) + f(x * 2, y)
# print(f(1, 21))

# def f(x, y):
#     if x == 22: return 0
#     if x > y: return 0
#     if x == y: return 1
#     if x < y: return f(x + 1, y) + f(x * 2, y)
# print(f(2, 15) * f(15, 31))


# def f(x, y):
#     if x > y: return 0
#     if x == y: return 1
#     if x < y: return f(x + 1, y) + f(x * 2, y) + f(x + 2, y)
# print(f(3, 9) * f(9, 11) * f(11, 13))

# def f(x, y):
#     if x > y: return 0
#     if x == y: return 1
#     if x < y: return f(x + 1, y) + f(x + 4, y) + f(x + 5, y)
# print(f(30, 46))


#  ЗАДАНИЕ 23
# def f(x, y):
#     if x == y: return 1
#     if x < y: return 0
#     if x> y: return f(x - 2, y) + f(x // 2, y)
# print(f(28, 10) , f(10, 1))

# def f(x, y):
#     if x < y: return 0
#     if x == y: return 1
#     if x > y: return f(x - 1, y) + f(x // 2, y)
# print(f(30, 8) * f(8, 1))

# def f(x, y):
#     if x < y: return 0
#     if x == y: return 1
#     if x > y: return f(x - 2, y) + f(x // 2, y)
# print(f(32, 14) * f(14, 1))

# def f(x, y):
#     if x > y: return 0
#     if x == y: return 1
#     )
#     if x < y: return f(x + 3, y) + f(x // 2, y)
# print(f(32, 14) * f(14, 1))
x = 34
x = str(x)
print(int(max(x)))