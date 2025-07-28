import numpy as np

# 1. Create a (6, 4) NumPy array representing sales (in thousands)
sales = np.array([
    [55, 62, 70, 58],
    [48, 75, 80, 65],
    [60, 82, 78, 70],
    [45, 58, 62, 50],
    [68, 72, 74, 69],
    [50, 55, 60, 53]
])

# 2. Find the sales data for the 3rd shop
shop_3_sales = sales[2]
print("Sales for the 3rd shop:", shop_3_sales)

# 3. Get the sales for all shops in the last quarter
last_quarter_sales = sales[:, -1]
print("Sales in the last quarter:", last_quarter_sales)  

# 4. Increase all sales in the first quarter by 10%
sales[:, 0] = sales[:, 0] * 1.10  # Increase first column by 10%
print("Updated sales with 10% increase in Q1:")
print(sales)

# 5. If any sales value is less than 50, change it to 50
sales[sales < 50] = 50
print("Updated sales with minimum value 50:")
print(sales)

# 6. Convert the array into a single-column format
sales_column = sales.reshape(-1, 1)
print("Sales in single-column format:")
print(sales_column)

# 7. Reshape it back to its original (6, 4) format
sales_reshaped = sales_column.reshape(6, 4)
print("Reshaped back to original form:")
print(sales_reshaped)
