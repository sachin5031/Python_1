n = [100, 11, 125, 151, 7, 35]
# Initialize minimum and maximum with the first element
minimum = n[0]
maximum = n[0]

for i in n:
    if i < minimum:
        minimum = i  # Update minimum if a smaller value is found
    if i > maximum:
        maximum = i  # Update maximum if a larger value is found

print(f"Smallest Value: {minimum}")
print(f"Largest Value: {maximum}")

#Using the minimum and maximum with functions methods

def find_min_max(n):
    # Initialize minimum and maximum with the first element
    minimum = n[0]
    maximum = n[0]
    min_index = 0
    max_index = 0

    # Loop through the list using index
    for i in range(0, len(n)):
        if n[i] < minimum:
            minimum = n[i]
            min_index = i  # Store the index of the minimum value
        if n[i] > maximum:
            maximum = n[i]
            max_index = i  # Store the index of the maximum value

    return minimum, min_index, maximum, max_index

# Example list
n = [100, 11, 125, 151, 7, 35]

# Function call
min_val, min_pos, max_val, max_pos = find_min_max(n)

# Print results
print(f"Smallest Value: {min_val} at Index: {min_pos}")
print(f"Largest Value: {max_val} at Index: {max_pos}")


def second_largest(numbers):
    first = second = float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

n = [100, 11, 125, 151, 7, 35]
result = second_largest(n)
print(result)