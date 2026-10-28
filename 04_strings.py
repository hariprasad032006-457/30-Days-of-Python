#single line comment
letter = 'p'
print(letter)
print(len(letter))
greeting = 'Hello , World!'
print(greeting)
print(len(greeting))

sentence = " i will complete this 30 days challenge"
print(sentence)

#multiline string
multiline_string  = ''' i am a student and i enjoy learning .
now i am studing b.tech 4 year in centurion univercity .
i love coding.'''

print(multiline_string)

multiline_string1 = """ i am a student and i enjoy learning .
now i am studing b.tech 4 year in centurion univercity .    
i love coding."""
print(multiline_string1)

#string concatenation
first_name = 'hari'
last_name = 'prasad'
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(full_name))
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))

# unpacking characters
language = 'python'
a,b,c,d,e,f = language
print(a) #p
print(b) #y
print(c) #t
print(d) #h
print(e) #o
print(f) #n

#accessing characters using indexing
language = 'python'
first_character = language[0]
print(first_character)
second_character = language[1]
print(second_character)
last_character = language[-1]
print(last_character)

# if we want to start from right end we can use negative indexing. -1 is the last index
language = 'python'
last_character = language[-1]
print(last_character)
second_last_character = language[-2]
print(second_last_character)

#slicing of string
language = 'python'
#starts at zero and up to 3 but nort includes 3
first_three = language[0:3]
last_three = language[3:6]
print(first_three)
print(last_three)
 # another way of slicing is to use negative indexing
language = 'python'
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2]
print(pto)  # pto


# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?')  # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)')  # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

# String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'thirty days of python'
print(challenge.capitalize())  # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'thirty days of python'
print(challenge.count('y'))  # 3
print(challenge.count('y', 3, 14))  # 1
print(challenge.count('th'))  # 2`

# endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion'))  # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10))  # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# format()	formats string into nicer output
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(
    first_name, last_name, job, country)
print(sentence)  # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi  # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result)  # The area of circle with 10 is 314.0

# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0
