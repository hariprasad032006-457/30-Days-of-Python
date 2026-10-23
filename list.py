#creating an empty list
my_list = list()
print(len(my_list))
 
# Another way to create an empty list
my_list = []
print(len(my_list))

heros = ['spiderman', 'ironman', 'hulk', 'thor', 'captain america']
print(heros)
print(len(heros))

# Get the first item, the middle item and the last item of the list

first_hero = heros[0]
print('First hero:', first_hero)
middle= len(heros) // 2
middle_hero = heros[middle]
print('Middle hero:', middle_hero)
last_hero = heros[-1]
print('Last hero:', last_hero)

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ['hari' , 20 , 5.3, 'single','36 Fuller Place, Prospect Avenue, Brooklyn']

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

print('Number of companies:', len(it_companies))

# Print the first, middle and last company
first_company = it_companies[0]
print('First company:', first_company)
middle_company = it_companies[len(it_companies) // 2]
print('Middle company:', middle_company)
last_company = it_companies[-1]
print('Last company:', last_company)

it_companies[0] = 'Meta'
print(it_companies)

it_companies.append('Twitter')
print(it_companies)

it_companies.insert(len(it_companies) // 2, 'LinkedIn')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

# Join the it_companies with a string 'servises;  
joined_companies = ' servises;  '.join(it_companies)
print(joined_companies)

print('Facebook' in it_companies)  # false
print('META' in it_companies)  # true

it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method

it_companies.reverse()
print(it_companies)
# another way to reverse the list is to use sort() method with reverse=True
it_companies.sort(reverse=True)
print(it_companies)


print(it_companies[0:3])  # first three companies
print(it_companies[-3:])  # last three companies


# Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
print(it_companies[middle_index])

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

#remove last IT company from the list
it_companies.pop() # you can write it_companies.pop(-1) also
# .pop() method removes the last item from the list by default
print(it_companies)

#Remove the middle IT company or companies from the list
it_companies.pop(middle_index)
print(it_companies)

it_companies.clear()  # this will remove all the items from the list
print(it_companies)

del it_companies  # this will delete the list completely

# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
     #or you can use extend() method to join the lists
#front_end.extend(back_end)
print(full_stack)
 
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)


#Exercises: Level 2

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(max(ages))  # maximum age
print(min(ages))  # minimum age

#Find the median age (one middle item or two middle items divided by two)
if len(ages) % 2 == 0:
    median_age = (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2
else:
    median_age = ages[len(ages) // 2]
print('Median age:', median_age)

#Find the average age (sum of all items divided by their number )
total_age = sum(ages)
average_age = total_age / len(ages)
print('Average age:', average_age)

for i in range(len(ages)):
    ages[i] = ages[i] - min(ages)
    
print('Ages after normalization:', ages)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
divide_index = len(countries) // 2
first_half = countries[:divide_index]
second_half = countries[divide_index:]
print('First half of countries:', first_half)
print('Second half of countries:', second_half)

 #['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

china, russia, usa, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print('China:', china)
print('Russia:', russia)
print('USA:', usa)
print('Scandic countries:', scandic_countries)