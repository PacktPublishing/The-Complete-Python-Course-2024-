# Access elements from a Nested Dictionary
# Code by studyopedia

products = {
  "mystock1" : {
   "Product": "SSD",
   "Price": 3000,
   "Quantity": 100,
   "InStock" : "Yes"
  },
  "mystock2" : {
   "Product": "HDD",
   "Price": 2500,
   "Quantity": 50,
   "InStock" : "Yes"
  },
  "mystock3" : {
   "Product": "Headphone",
   "Price": 2800,
   "Quantity": 40,
   "InStock" : "Yes"
  },
  "mystock4" : {
   "Product": "Earphone",
   "Price": 1500,
   "Quantity": 10,
   "InStock" : "No"
  }
}

print(products)

print(products["mystock2"]["Product"])
print(products["mystock4"]["Quantity"])




