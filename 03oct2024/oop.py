class Animal:
    _name = None  #protected
    __age = None #private
    _region = None

    # constructor
    def __init__(self, name, age, region): #init make constructor
        self._name = name
        self.__age = age
        self.region = region
    
    # def getDetail(self):
    #     return f'{self.name} is {self.age} years old and lives in {self.region}'
    def __str__(self): #str initiate at calling the class 
        return f'{self._name} is {self.__age} years old and lives in {self.region}'
    

    # setter
    def setName(self, new_name):
        self.name = new_name
    
    # getter
    def getName(self):
        return self.name
    
    def food(self):
        pass
    def abc(self):
        pass
    # # attribute
    # arg1 = "Dog"
    # arg2 = "Cat"


    # # methods
    # def func(self):
    #     print("This is a method in Animal class")


# objects of class
# anm1 = Animal()
anm1 = Animal('crow', 2, 'pakistan')
anm2 = Animal('hippo', 20, 'sea')
anm3 = Animal('cat', 201, 'soil')

# print(anm1.getDetail())
# print(anm2.getDetail())
# print(anm3.getDetail())
print(anm1)
print(anm2)
print(anm3)
# print(anm1.arg1)
# print(anm1.func())


# class Bio:
#     # attribute
#     fname = "muhammad"
#     lname = "abdullah"
#     age = 23
#     dob = '25 nov 2023'
#     edu = "BSCS"
#     location = "gulberg"
#     company = 'Axix Technologies'
#     email = 'abdullah.muhammad@axixtechnologies.com'   
#     phone_no = "03121574512"
#     designation = 'Software Engineer'
#     lead = "Danish Bashir"

    

#     def fullName(self):
#         return f'{self.fname} {self.lname}'
#     def work(self):
#         return f'{self.fullName()} is working as a {self.designation} in {self.company}'
#     def contact(self):
#         return f'Email: {self.email}, Phone No: {self.phone_no}'
#     def education(self):
#         return f'{self.fullName()} is studying {self.edu} in {self.location}'
#     def hierarchy(self):
#         return f'{self.fullName()} is under the team lead {self.lead} in {self.company}'


# # creating an object and accessing its methods and attributes

# data = Bio()

# print(f'fullname: {data.fullName()} ')

# print(f'Bio: {data.fullName()} is {data.age} years old, he was born in {data.dob}')

# print(f'Work: {data.work()}')

# print(f'Contact: {data.contact()}')

# print(f'Education: {data.education()}')

# print(f'Hierarchy: {data.hierarchy()}')



