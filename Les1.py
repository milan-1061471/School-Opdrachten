# Les 1
# Standaard operatoren
import math

print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(2 // 3)
print(2 ** 3)
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(3 ** 2)

# Haakjes
print(23.95 * 32.9)
print(23.95 * 32.9 + 6)
print((23.95 * 32.9) + 6)
print(23.95 * (32.9 + 6))
print(23.95 / 32.9)
print(23.95 / 32.9 + 6)
print((23.95 / 32.9) + 6)
print(23.95 / (32.9 + 6))

# Variabelen
name = "John Doe"
print(name)
street = 'Neverland Lane'
print(street)
items = 5
print(items)
price = 19.95
print(price)
students = 28
teachers = 3
seats = students + teachers
print(seats)
correct = students > teachers
print(correct)
incorrect = students > seats
print(incorrect)
line_character = '-'
line = line_character * 20
print(line)

# IDLE
city = 'Rotterdam'
print(city)
type(city)
residents = 623652
print(residents)
type(residents)
area = 324.1
print(area)
type(area)
# Formatted string, variabele in string weergeven
print(f'The city of {city} has {residents} on an area of {area} square kilometers')