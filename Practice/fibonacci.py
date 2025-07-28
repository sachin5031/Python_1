# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a, b = 0, 1
#         for i in range(2, n + 1):
#             a, b = b, a + b
#         return b

    
# fibonacci(5)
#output: 5
# fibonacci(10)
#output: 55

def fibonacci_series(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example usage
fibonacci_series(10)
# Output: 0 1 1 2 3 5 8 13 21 34


#Without using function
n = int(input("Enter the number of terms: ")) #10

a, b = 0, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
# Output: 0 1 1 2 3 5 8 13 21 34