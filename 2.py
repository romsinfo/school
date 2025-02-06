
# print('x y z w')
# for x in 0, увкеа:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 #  ((w -> y) -> x) V - z
#                 f = ((w <= y) <= x) or (not z)
#                 if f == 0:
#                     print(x, y, z, w)




# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((not x) and y and z and z and (not w)) or ((not x) and y and (not z) and (not(w))) or\
#                     (x and y and z and (not w))
#                 if f:
#                     print(x, y, z, w)


# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = not ((not w or z) and (not x or y)) or (y == w or (z and not x))
#                 # ((z <= y) and (not x <= w)) <= ((z = w) or (y and not x)));

#                 if f == 0:
#                     print(x, y,z , w)


                  #  ДОМИК - and 
# V - or
#  ПАЛАЧКА - это not 
  
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((z <= y) and ((not x) <= w)) <= ((z == w) or (y and (not x)))

#                 if f == 0:
#                     print(x, y,z , w)


# print('a, b, c, d')
# for a in 0, 1:
#     for b in 0, 1:
#         for c in 0, 1:
#             for d in 0, 1:
#                 #((a ∧ b) ≡ ¬c) ∧ (b → d)
#                 f = ((a and b) == (not c)) and (b <= d)
#                 if f == 1:
#                     print(a, b, c, d)




# print('x y w z')
# for x in 0, 1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = (not(x <= z)) or (y == w) or y
#                 if f == 0:
#                     print(x, y, w, z)


#  nomer 5
# for n in range(2, 1000):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = '10' + r
#     else:
#         r = '1' + r + '01'
#     r = int(r, 2)
#     if r > 516:
#         print(n)
#         break

#nomer 7
# 1024 * 960 * 13 * 160 / 1480064
# пиксели * i * кол-во / скорость

# nomer 8
#  слово ПАРУСА, НО ВТОРУЮ А ПИСАТЬ НЕ НАДО !!!!!!
# АПРСУ А НЕ АПРСУА !!!!!
# s = 'АПРСУ'
# n = 0
# for x1 in s:
#     for x2 in s:
#         for x3 in s:
#             for x4 in s:
#                 for x5 in s:
#                     w = x1+x2+x3+x4+x5
#                     n+=1
#                     if w.count('У') <= 1 and w.count('АА') == 0:
#                         print(n)
#                         break # 223





#  КОЛ-ВО ЧИСЕЛ НЕ ПРИВЫШАЮЩИХ 9 В 27 СИСТЕМЕ СЧИСЛЕНИЯ
# 14
# x = 2 * 729 ** 2014 + 2 * 243 ** 2016 - 2 * 81 ** 2018 + 2 * 27
# k =0 

# while x > 0:
#     if x % 27 > 9:
#         k += 1
#     x = x // 27
# print(k)


# for a in range(1000, 1, -1):
#     k = 1
#     for x in range(1, 1000):
#         f = (x % a != 0) <= ((x % 14 == 0) <= (x % 4 != 0))
#         k 

# import sys
# sys.setrecursionlimit(10000)

# def f(n):
#     if n == 1: return 1
#     if n > 1: return n * f(n - 1)
# print((f(2024) - f(2023) / f(2022))



# f = open('./9-227.txt')
# k = 0
# for s in f:
#     arr = sorted([int(x) for x in s.split()])
#     k+=1
#     ap = [x for x in arr if arr.count(x) == 2] # ПОВТОРЯЮЩЕЕСЯ
#     anp = [x for x in arr if arr.count(x) == 1]
    
#     if len(ap) == 2 and len(anp) == 2 and\
#         arr[-1] + arr[-2] > (arr[0] + arr[1]) * 2 and arr[-1] % arr[0] != 0:
#             k += 1

# f = open('9data\9-228.txt')
# k = 0
# print(k)
# for s in f:
#     arr = sorted([int(x) for x in s.split()])
#     k+=1
#     ap = [x for x in arr if arr.count(x) > 1] # ПОВТОРЯЮЩЕЕСЯ
#     anp = [x for x in arr if arr.count(x) == 1]
    
#     if len(ap) > 0 and arr[-1] not in ap and sum(ap) < sum(anp):
#         k+=1

# print(k)


# f = open('9data\9-181.txt')
# k = 0

# for s in f:
#     arr = sorted([int(x) for x in s.split()])
#     k+=1
#     ap = [x for x in arr if arr.count(x) > 1] # ПОВТОРЯЮЩЕЕСЯ
#     anp = [x for x in arr if arr.count(x) == 1]
#     n = arr[0] * arr[1] * arr[2]

#     if n % arr[-1] == 0:
#         k+=1



# f = open('9data\9-176.txt')
# k = 0

# for s in f:
#     arr = sorted([int(x) for x in s.split()])

#     ap = [x for x in arr if arr.count(x) > 1] # ПОВТОРЯЮЩЕЕСЯ
#     anp = [x for x in arr if arr.count(x) == 1]
#     n = arr[0] * arr[1] * arr[2]

#     if len(ap) > 0 and sum(anp) % 2 != 0:
#          k+=1

# print(k) # 322




# f = open('9data\9-188.txt')
# k = 0

# for s in f:
#     arr = sorted([int(x) for x in s.split()])

#     ap = [x for x in arr if arr.count(x) > 1] # ПОВТОРЯЮЩЕЕСЯ
#     anp = [x for x in arr if arr.count(x) == 1]
    
#     n = arr[0] * arr[1]
#     n2 = arr[1] * arr[2]
#     n3 = arr[0] * arr[2]
  
#     if(len(arr) > 0):
#         if str(n)[-1] == '4' or str(n2)[-1] == '4' or str(n3)[-1] == '4':
#          k+=1

# print(k) # 965



# f = open('17data/17-202.txt')
# s = [int(x) for x in f]
# c = []
# maxi = 0
# k=0
# for i in range(len(s) - 1):
#     if s[i + 1] > 0 and len(str(s[i + 1])) == 3 and str(s[i + 1])[-2:] == '12':
#         k+=1
#         print(s[i + 1] + s[i-1 + 1] + s[i+1 + 1])

# print(k) 
# 4196

# f = open('17data/17-5.txt')
# s = [int(x) for x in f]
# c = []
# maxi = 0
# k=0
# for i in range(len(s) - 1):
#         if str(s[i])[-1] == '5' and str(s[i + 1])[-1] == '5':
#             if(s[i] + s[i + 1] > maxi):
#                 maxi = s[i] + s[i + 1]
# print(maxi) 



# f = open('17data/17-4.txt')
# s = [int(x) for x in f]
# k=0
# for i in range(len(s) - 1):
#         if s[i] % 13 == 4 and s[i] % 8 == 1:
#             k+=1 
# print(k) 

# f = open('17data/17-4.txt')
# s = [int(x) for x in f]
# c = [x for x in s if x % 13 == 4 and x % 8 == 1]
# print(max(c), sum(c))



# f = open('17data/17-339.txt')
# s = [int(x) for x in f]
# c = []
# mn19 = min([x for x in s if x % 19 == 0 and x > 0])
# for i in range(len(s) - 1):
#     pair = s[i] + s[i + 1]
#     if pair < mn19:
#         c.append(pair)

# print(len(c), max(c))


# f = open('17data/17-380.txt')
# s = [int(x) for x in f]
# c = []
# mx25 = max([x for x in s if str(x).endswith('25')])
# for i in range(len(s) - 2): # -2 потому что брать ТРОЙКИ
#     s1 = (len(str(abs(s[i]))) == 4)
#     s2 = (len(str(abs(s[i + 1]))) == 4)
#     s3 = (len(str(abs(s[i + 2]))) == 4)
#     if (s1 + s2 + s3) < 3 and s[i] + s[i + 1] + s[i + 2] <= mx25:
#         c.append(s[i] + s[i + 1] + s[i + 2])

# print(len(c), max(c))

# f = open('17data/17-404.txt')
# s = [int(x) for x in f]
# c = []
# mn=min(s)
# for i in range(len(s) - 1):
#     if s[i] % 55 == mn or s[i + 1] % 55 == mn:
#         c.append(s[i] + s[i + 1])
# print(len(c), min(c))


# f = open('17data/17-407.txt')
# s = [int(x) for x in f]
# ln32 = [x for x in s if x % 32 == 0]
# c = []
# mn=min(s)
# for i in range(len(s) - 1):
#     if (s[i] < 0 or s[i + 1] < 0) and (s[i] + s[i + 1] < len(ln32)):
#         c.append(s[i] + s[i + 1])
# print(len(c), max(c))


# f = open('17data/17-4.txt')
# s = [int(x) for x in f]
# k = 0
# c = []
# for i in range(len(s)):
#     if s[i] % 3 == 0 and s[i] % 7 != 0 and s[i] % 17 != 0 and s[i] % 19 != 0 and s[i] % 27 != 0:
#         c.append(s[i])
#         k+=1
# print(k, max(c)) # 445


# f = open('17data/17-338.txt')
# s = [int(x) for x in f]
# mn = min(s)
# c = []
# k = 0
# for i in range(len(s) - 1):
#     if s[i] % 117 == mn or s[i + 1] % 117 == mn:
#         k+=1
#         c.append(s[i] + s[i + 1])
# print(k, max(c), len(c)) # 445



# f = open('17data/17-342.txt')
# s = [int(x) for x in f]
# mn37 = min([x for x in s if x % 37 % 2 == 0])
# mn73 = max([x for x in s if x % 73 % 2 == 0])
# # print(mn37, mn73) 100 995
# c = []
# k = 0
# for i in range(len(s) - 1):
#     g = 0
#     if mn37 < s[i] < mn73:
#         g+=1
#     if mn37 < s[i + 1] < mn73:
#         g+=1
#     if g == 1:
#         c.append(s[i] + s[i + 1])
# print(len(c), min(c)) # 445



# f = open('17data/17-379.txt')
# s = [int(x) for x in f]
# maxi = max([x for x in s if str(x).endswith('15')])
# c = []

# k = 0
# for i in range(len(s) - 2):
#     g  = 0
#     if len(str(s[i])) == 4:
#         g+=1
#     if len(str(s[i + 1])) == 4:
#         g+=1
#     if len(str(s[i + 2])) == 4:
#         g+=1
#     if (s[i] + s[i + 1] + s[i + 2] >= maxi) and g == 1:
#         k+=1
#         c.append(s[i] + s[i + 1] + s[i + 2])
# print(k, max(c), len(c)) # 445


# f = open('17data/17-403.txt')
# s = [int(x) for x in f]
# mn = min(s)
# # print(mn37, mn73) 100 995
# c = []
# k = 0
# for i in range(len(s) - 1):
#     if (s[i] + s[i + 1]) % 18 == mn:
#         c.append(s[i] + s[i + 1])
# print(len(c), max(c)) # 445


# f = open('17data/17-298.txt')
# s = [int(x) for x in f]
# mn = max([x for x in s if x % 197 == 0])
# # print(mn37, mn73) 100 995
# c = []

# for i in range(len(s) - 1):
#     g = 0
#     strNum = str(s[i])
#     strNum = sorted(strNum)
    
#     for j in range(len(strNum)):
#         if(j * 197 == strNum[len(strNum) - j]):
#             g+=1
#     if g == 1 and (s[i] + s[i + 1]) < mn:
#         c.append(s[i] + s[i + 1])

# print(len(c), max(c))

# ОТВЕТЫ = 2, 41
#   НОМЕР 9
# f = open('Копия 09-1.txt')
# k = 0
# for s in f:
#     a = sorted([int(x) for x in s.split()]) # [1, 2, 3, 4]
#     sm1 = sum(a[1:])
#     a1 = a[1] * a[2]
#     a2 = a[0] * a[3]
#     a3 = a[0] * a[2]
#     a4 = a[1] * a[3]

#     if a[0] * 5 < sm1 and (a1 == a2 or a3 == a4):
#         k += 1
# print(k) # 9


# f = open('Копия 09-2.txt')
# k = 0
# for s in f:
#     a = sorted([int(x) for x in s.split()]) # [1, 2, 3, 4]
#     sm1 = sum(a[1:])

#     if a[0] ** 2 > sm1 and (a[0] % 2 != 0 and a[1] % 2 != 0 and a[2] % 2 != 0 and a[3] % 2 != 0):
#         k += 1
# print(k) # 41


f = open('17-3.txt')
s = [int(x) for x in f]

# c = []
# k = 0
# for i in range(len(s) - 1):
#     if (s[i] % 2 != 0 and str(s[i])[-1] == str(s[i + 1])[-1]):
#         c.append(abs(s[i]) * abs(s[i + 1]))
# print(len(c), max(c)) # 445


# f = open('17-4.txt')
# s = [int(x) for x in f]

# c = []
# k = 0

# mn700 = min([x for x in s if str(x).endswith('700')])

# for i in range(len(s) - 2):
#     g = 0
#     if len(str(s[i])) == 5:
#         g+=1
#     if len(str(s[i + 1])) == 5:
#         g+=1
#     if len(str(s[i + 2])) == 5:
#         g+=1
#     if g <= 2 and s[i] + s[i + 1] + s[i + 2] >= mn700:
#         c.append(s[i] + s[i + 1] + s[i + 2])
# print(len(c), min(c)) # 1465 -698




# arr = [12, 16, 64, 56, 129]
# count1 = min([bin(x)[2:].count('1') for x in arr])
# arr2 = max([x for x in arr if bin(x)[2:].count('1') == count1])
# print(arr2)
