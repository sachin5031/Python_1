#Using Zipfile method

# import zipfile
# with zipfile.ZipFile("python_course.zip","w") as archive:
#     archive.write("test1.txt")
#     archive.write("test3.txt")
#     archive.write("test2.txt")

# with zipfile.ZipFile("python_course.zip","r") as archive:
#     archive.extractall("extracted_files") #it will extract all files in the zip file

import os

# os.mkdir("courses") # Create a new directory named "courses"
# print(os.getcwd())  # List current directory
# print(os.path.exists("courses")) # Check if the directory exists
# os.chdir("courses") # Change the current working directory to "courses"
# print(os.getcwd()) # List the current directory
# print(os.listdir()) # List files in the current directory
# os.rmdir("courses") # Remove the directory "courses"

# os.remove("test.txt")

files=["test1.txt","test3.txt","test2.txt"]

for each_files in files:
    os.remove(each_files)