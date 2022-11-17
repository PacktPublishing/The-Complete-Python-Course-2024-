# Keep only duplicate items in two sets
# Code by studyopedia

myset1 = {"amit", "john", "kane", "warner", "steve"}
print(myset1)

myset2 = {"jacob", "john", "mark", "anthony", "steve"}
print(myset2)

myset1.intersection_update(myset2)
print(myset1)