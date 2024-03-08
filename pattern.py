# create a for loop for 9 lines, start with 1 star and add a star on every row
# if statement to stop adding stars after 5th row/loop
# else statement to take away a star at each line starting with 4 stars on 6th row/loop
# printing a smaller index as the loop goes on till the end

star = "*"

for i in range (1,10):
    
    if i < 6:
        print (star)
        star = star + "*"

    else:
        index = i-4
        print (star[index:])
