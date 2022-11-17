# Can we update Tuple values
# Code by studyopedia

mytuple = ("Amit", "Craig", "Ronaldo", "Messi", "Tom", "Jacob")
print(mytuple)

# list
mylist = list(mytuple)

mylist[0] = "Zidane"
mylist[1] = "Beckham"
print("Updated List = ",mylist)

mytuple = tuple(mylist)
print("Updated Tuple = ",mytuple)
