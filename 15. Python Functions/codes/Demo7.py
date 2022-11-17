# Variable-length/ Arbitrary Arguments in Python (*args) (Example2)
# Code by studyopedia

def demo(*sports):
  print("Displaying passed arguments...")

  for name in sports:
      print(name)

# call
demo("Football", "Hockey", "Cricket", "Squash", "Volleyball")