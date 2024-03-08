# ask user to enter a number
# total will start at 0 and will add entered number after every loop
# count will start at 0 and will add 1 after each time a number is entered
# average is total of entered numbers divided by count excluding when -1 is entered

number = int(input("Please enter a whole number: "))

total = 0
count = 0

while number != -1:
     total += number
     count += 1
     number = int(input("Please enter a whole number: ")) 

     if number == -1:
          average = (total)/(count)
          print ("The average of all numbers entered is " + str(average))
          break
     
