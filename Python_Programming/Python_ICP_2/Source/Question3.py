# Write a python program to find the wordcountin a file for each line and thenprint the output.Finally store the output back to the file.
# Taking user input for file name and opening the file that user specified
fileName = input("Enter the name of file:")
word_frequency = {}
file = open(fileName, 'r')

# In this for loop for every line in the file converting into lowercase and by using Dictionary word, count are tracked
for line in file:
    words = line.lower().strip().split(" ")
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
file.close()

# The word frequency is written in the same file by opening the file in append mode
with open(fileName, 'a') as f:
    f.write("\n\nWord Frequency in this file is as below:")
    for word, count in word_frequency.items():
        f.write("\n{} = {}".format(word, count))
file.close()
