empty_tuple = ()
my_siblings = ('bhargavi','yesodha','jansi')
print(f'how many siblings do you have? {len(my_siblings)}')

empty_tuple = list(empty_tuple)
my_siblings = list(my_siblings)
my_siblings[0]= 'Narayana rao'
my_siblings[1] = 'santoshi kumari'
my_siblings.remove('jansi')
print(my_siblings)
my_parents = my_siblings.copy()
print(my_parents)
my_parents.append('bhargavi')
my_family = my_parents.copy()
print(f'My family members are: {my_family}')
my_siblings = tuple(my_siblings)



# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
print(tpl3)


brothers = ("Rahul", "Ravi")
sisters = ("Priya", "Sneha")
siblings = brothers + sisters

parents = ("Father", "Mother")
family_members = siblings + parents

*children, father, mother = family_members

print("Siblings:", children)
print("Father:", father)
print("Mother:", mother)


fruits = ("Apple", "Banana", "Mango")
vegetables = ("Carrot", "Potato", "Tomato")
animal_products = ("Milk", "Eggs", "Cheese")

food_stuff_tp = fruits + vegetables + animal_products

print(food_stuff_tp)

length = len(food_stuff_tp)

if length % 2 == 1:
    middle = food_stuff_tp[length // 2]
else:
    middle = food_stuff_tp[length // 2 - 1:length // 2 + 1]

print("Middle item(s):", middle)

nordic_countries = (
    "Denmark",
    "Finland",
    "Iceland",
    "Norway",
    "Sweden"
)

print("Estonia is Nordic:", "Estonia" in nordic_countries)
print("Iceland is Nordic:", "Iceland" in nordic_countries)
