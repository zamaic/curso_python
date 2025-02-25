p = 'calabaza'
adivinadas = set({'a','b'})
palabra = ''.join([letra if letra in adivinadas else '_' for letra in p])
print(palabra)

lunas = ['Luna', 'Ceres', 'Deimos', 'Phobos']

print(lunas[1:3])

menu = ['spaguetti','spam','spam','sopa','spam']

#menu = list(set(menu))
menu.remove('spam')

print(menu)