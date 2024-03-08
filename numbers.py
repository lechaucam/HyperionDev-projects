# Ask 3 times to enter a number as integer variable
first_number = int (input("Please enter a number: "))
second_number = int (input("Please enter a number: "))
third_number = int(input("please enter a number: "))

# calculate total of numbers and print sum and other calculations
sum_numbers =((first_number) + (second_number) + (third_number))
print(sum_numbers)
print((first_number)-(second_number))
print((third_number)*(first_number))
print((sum_numbers)/(third_number))

# different way to code the calculations, make a list of entered numbers
# make calculations with sum and print
number_list = [(first_number),(second_number),(third_number)]
print (sum(number_list))
# make calculations with indexposition in list and print
print (number_list[0]-number_list[1])
print (number_list[2]*number_list[0])
print (sum(number_list)/number_list[2])