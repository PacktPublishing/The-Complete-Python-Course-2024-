# Access values in a Python Dictionary using the get() method
# Code by studyopedia

mystock = {
    "Product":"Earphone",
    "Price": 800,
    "Quantity": 50,
    "InStock": "Yes"
}

print(mystock)

print(mystock.get("Product"))
print(mystock.get("InStock"))