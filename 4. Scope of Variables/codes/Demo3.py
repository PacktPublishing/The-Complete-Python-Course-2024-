# change the value of a global variable using global keyword
# Code by studyopedia

# outer
# global scope
a = 5

# Function definition
def demo():
    # inner
    global a
    a = 10
    print(a)

# call
demo()

# outer
print(a)