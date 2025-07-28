l1 = [12, 14, 67, 87, 90]
low = 0
high = len(l1) - 1
searchkey = 67
flag = False
while low <= high:
    mid = (low + high) // 2
    if l1[mid] == searchkey:
        flag = True
        break
    elif searchkey > l1[mid]:
        low = mid + 1
    else:
        high = mid - 1
if flag:
    print("Found")
else:
    print("Not Found")


#Binary search using Class 

class BinarySearch:
    def __init__(self, arr):
        self.arr = arr

    def search(self, target):
        left, right = 0, len(self.arr) - 1

        while left <= right:
            mid = (left + right) // 2  # Find the middle index
            if self.arr[mid] == target:
                return mid  # Target found
            elif self.arr[mid] < target:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half

        return -1  # Target not found

# Example usage
sorted_list = [1, 3, 5, 7, 9, 11]
binary_search = BinarySearch(sorted_list)

target = 7
result = binary_search.search(target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found.")
