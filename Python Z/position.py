numbers = [1, 2, 3, 4, 5]
key = 5
flag = False
pos = -1
N = len(numbers)
for i in range(0, N):
    if numbers[i] == key:
        flag = True
        pos = i
        break
if flag:
    print("Found", pos)
else:
    print("Not Found", pos)


#using Function Methods

def search_key(numbers, key):
    N = len(numbers)  # Get the length of the list
    for i in range(N):
        if numbers[i] == key:
            return i  # Return the index as soon as the key is found
    return -1  # Return -1 if the key is not found

# Example list and key to search
numbers = [1, 2, 3, 4, 5]
key = 5

# Function call
pos = search_key(numbers, key)

# Print result
if pos != -1:
    print(f"Found at Index: {pos}")
else:
    print("Not Found")
