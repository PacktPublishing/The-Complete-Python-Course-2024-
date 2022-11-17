# Arbitrary Keyword Arguments in Python (**kwargs)
# Code by studyopedia

def demo(**stu):
    print("Student name: "+stu["student"])
    print("Student section: "+stu["section"])

# call
demo(student = "Jack", section = "AD")


