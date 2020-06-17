class Employee:
    counter = 0
    salary_sum = 0

    # In this default constructor of employee class assigning values and counting the number of employees
    def __init__(self, n, f, s, d):
        self.name = n
        self.family = f
        self.salary = s
        self.department = d
        Employee.counter += 1
        Employee.salary_sum += s

    # Method for calculating average salary
    def get_salary_average(self):
        average_sal = self.salary_sum / self.counter
        print("The average salary is: " +str(average_sal))
        return
    # Method for displaying the results
    def details(self):
        print("\nName:"+self.name, "\nFamily:"+self.family,
              "\nSalary:" + str(self.salary), "\nDepartment:"+self.department)

# FullTimeEmployee class is created and inherited employee class
class FullTimeEmployee(Employee):
    def __init__(self, n, f, s, d):
        Employee.__init__(self, n, f, s, d)
    e1 = Employee("Pujitha", "Sakhavrapu", 560000, "Computer Science")
    e2 = Employee("Mounika", "Rachamadugu", 890000, "Computer Science")
    e1.details()
    e2.details()


e3 = Employee("Tejaswi", "Guturu", 180000, "Computer Science")
e4 = FullTimeEmployee("Pooja", "Gopu", 68000, "Computer Science")
e4.details()
e3.details()
Employee.get_salary_average(Employee)