# Question: Write a program, which reads weights (lbs.) of N students into a list and convert these weights to kilograms in a other list
# Two lists lbs and kgs
lbs = []
kgs = []
# Taking input from user for no, of students
total = int(input("Enter the number of students:"))

# In this for loop, taking inputs from user then inserting them lbs list  and converting them into kgs and inserting into kgs list
for i in range(total):
    lbs.append(float(input("Enter weight of {} student:".format(i + 1))))
    kgs = [i * 0.454 for i in lbs]

print("Student Weight in Lbs: {}\nStudent Weight in Kgs: {}".format(lbs, kgs))
