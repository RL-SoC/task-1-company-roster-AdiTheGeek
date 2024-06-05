"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""
from people import * # import everything!

if __name__ == "__main__":  # Equivalent to int main() {} in C++.
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number:"))

        if last_input == 1:
            name = input("Name:")
            age = int(input("Age:"))
            ID = int(input("ID:"))
            city = input("City:")
            branchcodes = input("Branch(es):")
            # How will you conver this to a list, given that
            # the user will always enter a comma separated list of branch codes?
            # eg>   2,5
            branchcodes = [int(inp.strip()) for inp in branchcodes.split(",")]
            position = input("Position:")
            salary = input("Salary:")
            # Create a new Engineer with given details.
            engineer = Engineer(name,age,ID,city,branchcodes,position,salary) # Change this

            engineer_roster.append(engineer) # Add him to the list! See people.py for definiton
            print(engineer_roster)
        
        elif last_input == 2:
            name = input("Name:")
            age = int(input("Age:"))
            ID = int(input("ID:"))
            city = input("City:")
            branchcodes = input("Branch(es):")
            branchcodes = [int(inp.strip()) for inp in branchcodes.split(",")]
            position = input("Position:")
            superior = input("Enter superior ID:")
            salary = int(input("Salary:"))
            # Create a new Salesperson with given details.
            salesman = Salesman(name,age,ID,city,branchcodes,position,superior,salary) 

            sales_roster.append(salesman) # Add him to the list! See people.py for definiton
        

        elif last_input == 3:
            ID = int(input("ID: "))
            # Print employee details for the given employee ID that is given. 
            
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if int(employee.ID) == int(ID):
                    found_employee = employee
                    break
            
            if  not found_employee: print("No such employee")
            else:
                print(f"Name: {found_employee.name} and Age: {found_employee.age}")
                print(f"City of Work: {found_employee.city}")

                ## Write code here to list the branch names to
                ## which the employee reports as a comma separated list
                ## eg> Branches: Goregaon,Fort
                branch_names = []
                for i in found_employee.branches:
                    branch_names.append(branchmap[i]["name"])

                x = ", ".join(branch_names)
                print(f"Branches: {x}" )
                
                print(f"Salary: {found_employee.salary}")
                print(f"Position: {found_employee.position}")

        elif last_input == 4:
            #### NO IF ELSE ZONE ######################################################
            # Change branch to new branch or add a new branch depending on class
            # Inheritance should automatically do this. 
            # There should be no IF-ELSE or ternary operators in this zone
            ID = int(input("ID: "))
            new_branch = int(input("Branch to migrate to: "))

            found_employee = None
            for employee in engineer_roster + sales_roster:
                if int(employee.ID) == int(ID):
                    found_employee = employee
                    print(found_employee)
                    break
            
            found_employee.migrate_branch(new_branch)
            #### NO IF ELSE ZONE ENDS #################################################

        elif last_input == 5:
            ID = int(input("Enter Employee ID to promote: "))
            # promote employee to next position
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if int(employee.ID) == int(ID):
                    found_employee = employee
                    break
            x = found_employee.pre_defined_positions.index(found_employee.position)
            promotion_pos = found_employee.pre_defined_positions[x+1]
            found_employee.promote(promotion_pos)

        elif last_input == 6:
            ID = int(input("Enter Employee ID to give increment: "))
            amt = int(input("Enter the increment amount: "))
            # Increment salary of employee.
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if int(employee.ID) == int(ID):
                    found_employee = employee
                    break
            
            found_employee.increment(amt)
        
        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
            # Print superior of the sales employee.
            found_employee = None
            for employee in sales_roster:
                if int(employee.ID) == int(ID):
                    found_employee = employee
                    break
            
            found_employee.find_superior()

        elif last_input == 8:
            ID_E = int(input("Enter Employee ID to add superior: "))
            ID_S = int(input("Enter Employee ID of superior: "))
            # Add superior of a sales employee

            found_employee = None
            for employee in sales_roster:
                if int(employee.ID) == int(ID_E):
                    found_employee = employee
                    break
            
            found_employee.add_superior(ID_S)

        else:
            raise ValueError("No such query number defined")
