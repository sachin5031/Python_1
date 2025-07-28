import numpy as np

def create_matrix(name):
    try:
        rows = int(input(f"Enter the number of rows for Matrix {name}: "))
        cols = int(input(f"Enter the number of columns for Matrix {name}: "))
        print(f"Enter the elements for Matrix {name}:")
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                val = int(input(f"Element at ({i+1},{j+1}): "))
                row.append(val)
            matrix.append(row)
        return np.array(matrix)
    except ValueError:
        print("Invalid input! Only integers are allowed.")
        return None

def addition(a, b):
    if a.shape == b.shape:
        return a + b
    else:
        return "Error: Matrices must have the same dimensions."

def subtraction(a, b):
    if a.shape == b.shape:
        return a - b
    else:
        return "Error: Matrices must have the same dimensions."

def multiplication(a, b):
    try:
        return np.dot(a, b)
    except ValueError:
        return "Error: Cannot multiply these matrices."

def division(a, num):
    try:
        return a / num
    except ZeroDivisionError:
        return "Error: Division by zero."

# --- Main Program ---

matrix_a = create_matrix("A")
matrix_b = create_matrix("B")

if matrix_a is None or matrix_b is None:
    print("Exiting due to invalid input.")
    exit()

print("\nMatrix A:\n", matrix_a)
print("\nMatrix B:\n", matrix_b)

while True:
    print("\nMatrix Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division of Matrix A by a number")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            print("Result:\n", addition(matrix_a, matrix_b))
        elif choice == 2:
            print("Result:\n", subtraction(matrix_a, matrix_b))
        elif choice == 3:
            print("Result:\n", multiplication(matrix_a, matrix_b))
        elif choice == 4:
            number = int(input("Enter the number to divide Matrix A: "))
            print("Result:\n", division(matrix_a, number))
        elif choice == 5:
            print("Thank you! Exiting the calculator.")
            break
        else:
            print("Invalid choice. Please choose between 1 and 5.")
    except ValueError:
        print("Please enter a valid number.")
