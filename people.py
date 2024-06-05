"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    name : str 
    age : int
    ID : int
    city : str
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10_000 
    
    def change_city(self, new_city:str):
        # Change the city 
        if new_city != self.city:
            self.city = new_city
            return True
        return False
        # Return true if city change, successful, return false if city same as old city

    def migrate_branch(self, new_code:int):
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        if len(self.branches) == 1:
            x = branchmap[self.branches[0]]["city"]
            y = branchmap[new_code]["city"]
            if x == y:
                self.branches = new_code
                return True
            else:
                return False
        else:
            print("Works at multiple branches")
            return False
        # Change old branch to new if it is in the same city, else return false.

    def increment(self, increment_amt: int):
        # Increment salary by amount specified.
        self.salary = self.salary + increment_amt


class Engineer(Employee):
    position : str # Position in organization Hierarchy
    increment_bonus = 1.1
    promotion_increment = 0.3
    pre_defined_positions = ["Junior","Senior","Team Lead","Director"]
    
    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        assert position in self.pre_defined_positions, f"Postion {position} is not one of the pre-defined positions"
        # Only then set the position. 
        self.position = position
        print("An Engineer object has been created.")

    
    def increment(self, amt:int):
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
        self.salary = int(float(self.salary) + float(amt) * self.increment_bonus)
        
    def promote(self, position:str):
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        current_rank = self.pre_defined_positions.index(self.position)
        future_rank = self.pre_defined_positions.index(position)
        if future_rank > current_rank:
            self.position = position
            self.increment(int(float(self.salary)*self.promotion_increment))
            return True
        else:
            return False

class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to
    increment_bonus = 1.05
    promotion_increment = 0.3
    pre_defined_positions = ["Rep","Manager","Head"]
    all = []
    
    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Rep", superior = None, salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        
        # Check if position is one of  "Rep", "Manager", "Head" 
        assert position in self.pre_defined_positions, f"Postion {position} is not one of the pre-defined positions"
        # Only then set the position. 
        self.position = position
        self.superior = superior
        Salesman.all.append(self)
    
    def increment(self, amt:int):
        # While other functions are the same for and engineer,
        # and increment to an salesman's salary should add a 5% bonus on to "amt"
        self.salary = int(float(self.salary) + float(amt) * self.increment_bonus)
   
    def promote(self, position:str):
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        current_rank = self.pre_defined_positions.index(self.position)
        future_rank = self.pre_defined_positions.index(position)
        if future_rank > current_rank:
            self.position = position
            self.increment(int(float(self.salary)*self.promotion_increment))
            return True
        else:
            return False

    def find_superior(self):
        if self.superior is None:
            return None  # Handle cases where no superior is assigned

        else:
            for i in self.all:
                if int(i.ID) == int(self.superior):
                    print(f"The superior ID is:{i.ID} and the name is : {i.name}")
                    return i.ID, i.name
            
    def add_superior(self, superior_ID:int):
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,
        x = self.pre_defined_positions.index(self.position)
        for i in self.all:
            if int(i.ID) == int(superior_ID):
                print(i.position, self.position)
                y = self.pre_defined_positions.index(i.position)
                if y > x:
                    self.superior = superior_ID
                    print("Superior has been assigned.")
                    return True
                else:
                    print("Incorrect heirarchy.")
                    return False
        print("The superior employee doesn't exist.")
        return False    


    def migrate_branch(self, new_code: int):
        # This should simply add a branch to the list; even different cities are fine
        x = 0
        for i in self.branches:
            if new_code == i:
                x = 1
        if x == 0:
            self.branches.append(new_code)
            return True
        else:
            print("The employee already works in the newly assigned branch.")
            return False
