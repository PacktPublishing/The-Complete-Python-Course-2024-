# Keep all the items in the two sets except the duplicates
# Code by studyopedia

myset1 = {"amit", "john", "kane", "warner", "steve"}
print(myset1)

myset2 = {"jacob", "john", "mark", "anthony", "steve"}
print(myset2)

myset1.symmetric_difference_update(myset2)
print(myset1)
