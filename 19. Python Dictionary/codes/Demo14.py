# Delete a key and return the corresponding value
# Code by studyopedia

mystock = {
    "Product": "Earphone",
    "Price": 800,
    "Quantity": 50,
    "InStock": "Yes"
}

print(mystock)

# delete
result = mystock.pop("Quantity")
print("Corresponding value with popped key Quantity = ",str(result))

print("Updated Dictionary = \n", mystock)
