# call string variable 'quote'
# create for loop to change every second letter/position into lower case and others into upper case and print new_quote

quote = "Not all those who wander are lost"
new_quote = ""

for i in range(len(quote)):

    if i % 2 == 1:
        new_quote += quote[i].lower()

    else:
        new_quote += quote[i].upper()

print (new_quote)

# in order to change every other word we need to make a list of the words in the string 'quote', using split format
# print list for clarity

split_quote = quote.split(" ")
print(split_quote)

# create for loop to change every second word in list into upper case and others into lower case and add a space after each word
# join al words from list again into sentence called 'final quote'

final_quote = ""
for i in range(len(split_quote)):

    if i % 2 == 1:
        final_quote += split_quote[i].upper() + " "

    else:
        final_quote += split_quote[i].lower() + " "

print ("".join(final_quote))
