
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




