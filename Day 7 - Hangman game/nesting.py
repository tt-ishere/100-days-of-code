  #nesting dics in lists
travel_log = [
    { "Country": "france", 
      "cities_visited": ["Paris", "lille", "Dijon"], 
      "total_visits" : 12
    },
    { "Country": "Germany", 
      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
      "total_visits" : 5
    },
]

def add_new_country(x, y, z):
    new_travel ={}
    new_travel["Country", "Cities_visted", "total_visits"] = x, z, y
#    new_travel["Cities_visted"] = z
#    new_travel["total_visits"] = y
    
#    travel_log.append(new_travel)

#def add_new_country(x,y,z):
#    travel_log.append("Country", "Cities_visited", "total_visits") = x, z, y

# call function 
add_new_country("Russia", 2, ["Moscow", "Saint Pettersburg"])
print(travel_log)