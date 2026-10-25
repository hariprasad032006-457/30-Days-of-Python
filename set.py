room = {'hari','pavan'}
print(f'does the person in room : {'pavan' in room}')
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}

print(fruits)


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('twitter')
it_companies.update(['infosis','paytm'])
it_companies.pop()
it_companies.remove('IBM')
print(it_companies)
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.isdisjoint(st1) )# False
print(st2.difference(st1))
print(st2.issubset(st1))
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers)) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# python ^ dragon
