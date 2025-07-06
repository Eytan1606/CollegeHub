class Course:
    def __init__(self, code, name,credits):
        self.code = code
        self.name = name
        self.credits = credits
    
    def to_dict(self):
        return vars(self)

class Lecturer:
    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department =  department
    
    def to_dict(self):
        return vars(self)

class Student:
    def __init__(self, id, name,degree):
        self.id = id
        self.name = name
        self.degree = degree

    def to_dict(self):
        return vars(self)
    
    
