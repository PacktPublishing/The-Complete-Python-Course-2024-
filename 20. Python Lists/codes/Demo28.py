# Add elements to the end of the Multi-Dimensional Lists
# Code by studyopedia

mylist = [[10], [50, 60], [80], [90, 100, 200]]

print("Multidimensional List")
for res in mylist:
    print(res)

mylist.append([250, 275, 300])

print("\nUpdated Multidimensional List")
for res in mylist:
    print(res)