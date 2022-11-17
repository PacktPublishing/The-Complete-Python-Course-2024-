# Delete keys from the Dictionary
# Code by studyopedia

mystock = {
    "Product": "Earphone",
    "Price": 800,
    "Quantity": 50,
    "InStock": "Yes"
}

print(mystock)

del mystock["InStock"]

print("Updated Dictionary = \n", mystock)
