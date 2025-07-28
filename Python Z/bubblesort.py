# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]  

# numbers = [64, 34, 25, 12, 22, 11, 90]
# sorted_numbers = bubble_sort(numbers)
# print("Sorted list:", sorted_numbers)

#Using class 

class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
        return self.arr

numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sorter = BubbleSort(numbers)
sorted_numbers = bubble_sorter.sort()
print("Sorted list:", sorted_numbers)