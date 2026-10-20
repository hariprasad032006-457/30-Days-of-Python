# Variables in Python
first_name = 'hari'
last_name = 'prasad'
country = 'india'
city = 'vizag'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'hari',
   'lastname':'prasad',
   'country':'india',
   'city':'vizag'
   }
print('First Name:', first_name)
print('Last Name:', last_name)
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Is Married:', is_married)
print('Skills:', skills)
print('Person Info:', person_info)
print('Type of first_name:', type(first_name))
print('Type of age:', type(age))
print('Type of is_married:', type(is_married))
print('Type of skills:', type(skills))
print('Type of person_info:', type(person_info))

#Multiple variables can also be declared in one line:

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#Getting user input using the input() built-in function.
# Let us assign the data we get from a user into first_name and age variables. Example:
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)





#Check Data types:
# To check the data type of certain data/variable we use the type Examples:
# Different python data types
# Let's declare variables with various data types

first_name = 'hari'     # str
last_name = 'prasad'       # str
country = 'india'         # str
city= 'vizag'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('hari'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'hari '})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip


# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_str)    # Then convert the float to an integer
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'hari'
print(first_name)               # 'hari'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['h', 'a', 'r', 'i']