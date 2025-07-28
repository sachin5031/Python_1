# def valid_square(num):
#     square = int(num**0.5)
#     if square**2==num:
#         print(True) 
#     else:
#         print(False) 

# valid_square(10)
# # False
# valid_square(36)
# # True

def valid_square(num):
    square = int(num**0.5)
    return square**2 == num  # Returns True or False

print(valid_square(10))  # False
print(valid_square(36))  # True
