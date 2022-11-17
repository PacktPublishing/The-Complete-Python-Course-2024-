# Variable-length/ Arbitrary Arguments in Python (*args) (Example1)
# Code by studyopedia

def demo(*sports):
    print("Sports 1 = ",sports[0])
    print("Sports 2 = ",sports[1])
    print("Sports 3 = ",sports[2])

# call
demo("Football", "Hockey", "Cricket")

