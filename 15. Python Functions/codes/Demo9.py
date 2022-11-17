# Recursion in Python
# Code by studyopedia

def cal(num):

    if num == 0:
        return 1
    else: return num * cal(num-1)

# call
print("0! = ",cal(0))
print("1! = ",cal(1))
print("7! = ",cal(7))
print("10! = ",cal(10))