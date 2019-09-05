# Giraudo Francesco Es 39 Study Drill 1

# create a mapping of state to abbreviation
states = {
    'Italy':'IT',
    'France':'FR',
    'Germany':'DE',
    'Spain':'ES',
    'Netherland':'NL'
}

# create a basic set of states and some cities in them
cities = {
    'IT' : 'Milano',
    'FR' : 'Paris',
    'NL' : 'Rotterdam'
}

# add some more cities
cities['NL'] = 'Amsterdam'  # sobstitution of Rotterdam with Amsterdam
cities['ES'] = 'Sevilla'
cities['DE'] = 'Berlin'

# print out some cities
print('-' * 10)
print("IT state has ", cities['IT'])
print("ES state has ", cities['ES'])

# print some states
print("-"*10)
print("Germany's abbreviation is: ", states['Germany'])
print("France's abbreviation is: ", states['France'])

# do it by using the state then cities dict
print('-' * 10)
print("Netherland has: ", cities[states['Netherland']])
print("Italy has: ", cities[states['Italy']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)

# safely get a abbreviation by state that might not be there
state = states.get('Portugal')
