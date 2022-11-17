# Remove an item from the set using the discard() method
# Code by studyopedia

myset = {"amit", "john", "kane", "warner", "steve"}
print(myset)

myset.discard("warner")

# no error thrown for removing an item not in the list
# myset.discard("jacob")

print("\nUpdated Set = ",myset)
