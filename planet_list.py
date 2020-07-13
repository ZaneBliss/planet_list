planet_list = ['Mercury', 'Mars']

planet_list.append('Neptune')
planet_list.append('Jupiter')
planet_list.extend(['Saturn', 'Uranus'])
planet_list.insert(-1, 'Earth')
planet_list.insert(-1, 'Venus')
planet_list.append('Pluto')
rocky_planets = planet_list[:4]
planet_list.__delitem__(-1)