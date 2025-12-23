grocery_items = "milk, eggs, cheese, bread, apples"

# String slicing (based on character positions in the given string)
dairy1 = grocery_items[0:4]        # "milk"
dairy2 = grocery_items[13:19]      # "cheese"
bakery1 = grocery_items[21:26]     # "bread"

# String concatenation to build the sentence
message = "We have dairy and bakery items: " + dairy1 + ", " + dairy2 + ", and " + bakery1 + " in aisle 5"

print(message)
