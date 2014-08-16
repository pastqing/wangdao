# --coding:utf-8 --

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

print cities.items()

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found"

# 字典里可以添加函数
cities['_find'] = find_city

while True:
    print "State?(Enter to quit)",
    state = raw_input("> ")
    if not state: break
    
    city_found = cities['_find'](cities, state)
    print city_found
