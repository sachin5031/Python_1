#List Comprehension 3d
# x = int(input("Enter X value: "))
# y = int(input("Enter y Value: "))
# z = int(input("Enter Z Value: "))
# n = int(input("Enter n Value: "))

# list = []
# for i in range(x + 1):
#   for j in range(y + 1):
#     for k in range(z + 1):
#      if i + j + k != n:
#         list.append([i, j, k])
# print(list)


#List Comprehension 2d
# x = int(input("Enter X value: "))
# y = int(input("Enter y Value: "))
# n = int(input("Enter n Value: "))

# list = []
# for i in range(x + 1):
#   for j in range(y + 1):
#      if i + j != n:
#         list.append([i, j])
# print(list)

#List Comprehension 3d using function
def generate_combinations(x, y, z, n):
    result = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    result.append([i, j, k])
    return result

# Input values
x = int(input("Enter X value: "))
y = int(input("Enter Y value: "))
z = int(input("Enter Z value: "))
n = int(input("Enter N value: "))

# Generate and print the combinations
combinations = generate_combinations(x, y, z, n)
print(combinations)
