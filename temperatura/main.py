from calculadora_temp import ConversorTemperatura

print('''
[1] Celsius to Fahrenheit
[2] Fahrenheit to Celsius
''')

choice = input('Chose an option: ')
value = float(input('Type a value: '))

if choice == '1':
    result = ConversorTemperatura.celsius_to_fahrenheit(value)
elif choice == '2':
    result = ConversorTemperatura.fahrenheit_to_celsius(value)

print('Result:', result)