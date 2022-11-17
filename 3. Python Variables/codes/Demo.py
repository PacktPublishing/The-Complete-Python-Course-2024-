# Create a variable in Python
# Code by studyopedia

# a is of type int
a = 10

# b is of type string
b = "Amit"

# c is of type int
c = 25

print(a)
print(b)
print(c)

# Create a file if it does not already exist
file = open('E:\demo.txt', "w")
file.write("This is example text...")

# Read the content of the file
file = open('E:\demo.txt', "r")
print("Reading the contents of the file...\n",file.read())
