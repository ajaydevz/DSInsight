from datetime import datetime

class Person:
    def __init__(self,name,date_of_birth,location):
        self.name = name
        self.date_of_birth = date_of_birth
        self.location = location
        
    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year-((today.month,today.day) < (self.date_of_birth.month,self.date_of_birth.day))
        return age
        
p = Person("John", datetime(1994, 5, 15), "New York")
print(p.calculate_age())



from datetime import datetime

class Person:
    def __init__(self,name,date_of_birth,location):
        self.name = name
        self.date_of_birth = date_of_birth
        self.location = location

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth - ((today.month - today.day) < (self.date_of_birth.month - self.date_of_birth.day))
        return age
    
p = Person("john",datetime(1994,5,15),"new york")

