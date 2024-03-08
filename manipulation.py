# ask user to input a sentence and print length of the sentence
str_manip = input("please enter what's on your mind in one sentence: ")
print(len(str_manip))

# find last letter of the sentence and print the last letter
last_letter = (str_manip[-1])
print(last_letter)
# replace last letter with '@' and print sentence
print(str_manip.replace(last_letter,"@"))

# to print last 3 characters of the sentence backwards, it needs to be reversed and print 3 first letters
str_manip_reversed = str_manip[::-1]
print(str_manip_reversed[:3])

# concatenate first 3 letters of the sentence and last 2 letters and print the 5 letter word
five_letter_word = (str_manip[:3]) + (str_manip[-2:])
print(five_letter_word)