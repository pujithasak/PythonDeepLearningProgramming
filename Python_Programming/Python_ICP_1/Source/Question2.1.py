# Question: Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the resultant string and print it.
# Asking users for input string
string = input('Enter the string:')
# Slicing the input string and concatenating the sliced strings in order to delete specific characters
sub = string[0:3] + string[5:]
# Reversing the string and printing the output
print('Input String after deleting some characters and reverse the resultant string is "', sub[::-1],'"')
