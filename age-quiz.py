# Asking user to enter their age for the quiz
age = int(input("Please enter your age in numbers: "))

# Entered age will print a response from quiz
# criteria are above 100, 65-100,40-64, be exactly 21, under 13 and the rest

if age > 100: 
    print("Sorry, you're dead")
elif age >= 65: 
    print("Enjoy your retirement")
elif age >= 40: 
    print("You're over the hill")    
elif age == 21: 
    print("Congrats on your 21st!")
elif age >= 13:
    print("Age is but a number")
elif 0<= age < 13: 
    print("You qualify for the kiddie discount")
else: 
    print("Input is incorrect, please try again.")