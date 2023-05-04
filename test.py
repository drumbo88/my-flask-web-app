# type(<var>)
# del <var>

# None, Integer, Float

# Strings
print("Hello world")
print('Hello world')
print("""Hello world""")
print('''Hello world''')
print('Hello'+' world')

# Lists: son datos que generalmente pueden cambiar
colors = ['red', 'green', 'blue']

# colors.append('pink')
# colors.insert(1, 'white')
# colors.extend((len(colors), 'yellow'))
# colors.remove('green')
# colors.pop(-1)
# colors.index('redx') # num|error

# colors.sort(reverse=True)

print(colors)

# Tuples: son datos que NO cambian
x = (10, 20, 30)

# Dict (Diccionario, simil objeto)
locations = {
    (35.123,39.234): "Tokyo",
    (-20.123,39.234): "New York",
}
product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99,
}

# Sets: colección sin índices
colors = {'Red', 'Green', 'Blue'}
'Red' in colors # true
colors.add('Violet') # Al inicio
colors.remove('Red')
colors.clear() # Lo vacía