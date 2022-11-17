# Delete an element in a Dictionary with a specific key
# Code by studyopedia

mystock = {
    "Product": "Earphone",
    "Price": 800,
    "Quantity": 50,
    "InStock": "Yes"
}

print(mystock)

del mystock["Price"]

print("Updated Dictionary = \n", mystock)
