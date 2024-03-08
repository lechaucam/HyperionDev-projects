# creating  a menu list with 4 coffee items
# creating a 2 dictionaries with items(key) and stock and price (values)

menu = ["americano","cappuccino","latte","espresso"]
stock = { "americano" : 150,
         "cappuccino" : 50,
         "latte" : 40,
         "espresso" : 60
         }

price = { "americano" : 2,
         "cappuccino" : 3,
         "latte" : 4,
         "espresso" : 1
         }


# function to calculate stock value using keys: stock_value = (stock["americano"]) * (price["americano"])
# total_stock will add stock_value after each iteration and print total in the end.

total_stock= 0

for i in menu:
    stock_value = (stock[i]) * (price[i])
    total_stock += stock_value
    print (f"The stock value of {i} is {stock_value}£")

print (f"\nTotal stock value will be {total_stock}£")
