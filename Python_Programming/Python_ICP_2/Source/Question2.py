# Question: Write a program that returns every other char of a given string starting with first using a function
# This method will take input string as parameter and returns alternate character from the string
def string_alternative(input):
    return input[::2]


# In this main method taking input string from user and calling string_alternative method by passing the input string as parameter and the result is printed
def main():
    string = input("Enter the string:")
    print('Output is ' + string_alternative(string))


if __name__ == "__main__":
    main()
