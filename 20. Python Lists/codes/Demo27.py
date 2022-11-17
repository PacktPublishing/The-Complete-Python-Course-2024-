# Access elements in a Multidimensional Python Lists
# Code by studyopedia

mylist = [[10], [50, 60], [80], [90, 100, 200]]

print("Multidimensional List")
for res in mylist:
    print(res)

# 1st element of the 1st row
print("\n1st row 1st column\n",mylist[0][0])

# 1st element of the 2nd row
print("\n2nd row 1st column\n",mylist[1][0])

# 2nd element of the 2nd row
print("\n2nd row 2nd column\n",mylist[1][1])