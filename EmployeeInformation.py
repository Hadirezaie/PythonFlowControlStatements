numberOfEmployees = int(input("Enter number of employees: "))
employees = {}
for i in range(numberOfEmployees):
    name= input("Enter name: ")
    salary= int(input("Enter salary: "))
    employees[name] = salary

print("Now, enter an employee name to see the details: ")

while True:
    name = input("Enter name: ")
    if name not in employees:
        print("Employee with that name does not exist")
    else:
        print("The salary of employee with that name is: ", employees[name])
    choice = input("Do you want to add another employee? (y/n): ")
    if choice == "n":
        break