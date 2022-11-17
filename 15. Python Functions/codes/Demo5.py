# Default Arguments in Python
# Code by studyopedia

def details(name, rank = 10, score = 60.50):
    print("\nStudent Name = ", name)
    print("Student Rank = ", rank)
    print("Student Score = ", score)

# call
details(name = "Jack", rank = 5, score = 50.50)
details(name = "Tim")
details(name = "Will", rank = 7)



