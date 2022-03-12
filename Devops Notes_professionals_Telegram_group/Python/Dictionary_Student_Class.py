


 #Dictionary And thier uses

#How to define a dictionary

dict = {
    'name':"Deepak",
    'name1':"Mithun"
}

print dict['name_1']

dict[3] = "Nishant"

print dict

print "keys", dict.keys()
print "values:", dict.values()
print "has key" , dict.has_key(3)
iteritem = dict.iteritems()
print list(iteritem)
itervalues = dict.itervalues()
print list(itervalues)
iterkeys = dict.iterkeys()
print list(iterkeys)
del dict[3]

print dict

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print every state abbreviation

#for states, abbrev in states.items():
#    print "%s is abbreviated as : %s" % (states, abbrev)

for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

for state, abbrev in states.items():
    print "%s is abbreviated as : %s and has city %s" % (states, abbrev, cities[abbrev])

#Do some get

state1 = states.get('Oregon1', "does not exist")

print state1



