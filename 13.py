#  ip адрес  0-255.0-255.0-255.0-255
#  0-255 = 8бит
#  4 БАЙТА ЭТО ВСЕ

#  ЖУКОВА 13 - 109
# МАСКА  13 109
# МАСКА  13 000   -  8 квартир

# 11111000,00000000
# ОДИНАДЦАТЬ 0 ЗНАЧИТ 2 ** 11
# маска разделяет ip адрес сети от остальных

# 0.0.0.0  один 0 = 8



# ip = '10.8.248.131'
# mask = '255.255.224.0'
# res = '10.8.224.0'
# word = 'fade'



# uz = 0
# k1ip = sum([bin(x)[2:].count('1') for x in [204, 16, 168, 0]])
# k0m = 32 - sum([bin(x)[2:].count('1') for x in [255, 255, 248, 0]])

# for i in range(2 ** k0m):
#     k1 = bin(i)[2:].count('1')
#     if (k1ip + k1) % 5 != 0:
#         uz += 1
# print(uz) 
#1663


# uz = 0
# k1ip = sum([bin(x)[2:].count('1') for x in [200, 33, 100, 0]])
# k0m = 32 - sum([bin(x)[2:].count('1') for x in [255, 255, 248, 0]])

# for i in range(2 ** k0m):
#     k1 = bin(i)[2:].count('1')
#     if (k1ip + k1) % 7 != 0:
#         uz += 1
# print(uz) 
# 1586


# uz = 0
# k1ip = sum([bin(x)[2:].count('1') for x in [210, 66, 110, 0]])
# k0m = 32 - sum([bin(x)[2:].count('1') for x in [255, 255, 252, 0]])

# for i in range(2 ** k0m):
#     k1 = bin(i)[2:].count('1')
#     if (k1ip + k1) % 6 != 0:
#         uz += 1
# print(uz) 
# 894


# uz = 0
# k1ip = sum([bin(x)[2:].count('1') for x in [63, 7, 215, 0]])
# k0m = 32 - sum([bin(x)[2:].count('1') for x in [255, 255, 252, 0]])

# for i in range(2 ** k0m):
#     k1 = bin(i)[2:].count('1')
#     if (k1ip + k1) % 8 != 0:
#         uz += 1
# print(uz) 
# 1004


# uz = 0
# k1ip = sum([bin(x)[2:].count('1') for x in [210, 66, 110, 0]])
# k0m = 32 - sum([bin(x)[2:].count('1') for x in [255, 255, 252, 0]])

# for i in range(2 ** k0m):
#     k1 = bin(i)[2:].count('1')
#     if (k1ip + k1) % 6 != 0:
#         uz += 1
# print(uz) 

str = '1111001101'
print(str.split('0'))

uz = 0
k1ip = sum([bin(x)[2:].count('1') for x in [142, 108, 56, 118]])
k2ip = sum([bin(x)[2:].count('1') for x in [142, 108]])
kLst2ip = sum([bin(x)[2:].count('1') for x in [56, 118]])

k0m = 32 - sum([bin(x)[2:].count('1') for x in [255, 255, 252, 240]])

for i in range(2 ** k0m):
    k1 = bin(i)[2:].count('1')
    if k2ip < kLst2ip:
        uz += 1
print(uz) 