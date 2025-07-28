def gcd(a, b, c):
    while b != 0:
        a, b = b, a % b
    while c != 0:
        a, c = c, a % c
    return a

print(gcd(60, 78, 45))

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# print(gcd(60, 78))