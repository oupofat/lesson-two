'''Degree Conversion Calculator 3
Combine the 2 previous calculators into one program. First ask them to enter a number: either 1 or 2. If they entered 1, ask for the temperature in Fahrenheit and convert it to Celsius. If they entered 2, ask for the temperature in Celsius and convert it to Fahrenheit.'''

either = int(input("Enter 1 for fahrenheit and 2 for celsius."))
if either == 1:
    fahren = int(input("What is the temperature in fahrenheit?"))
    fahren = (fahren - 32)*.55556
    print("The temperature in celsuis is",fahren,".")
else:
    celsius = int(input("What is the temperature in celsius?"))
    celsius = (celsius * 1.8)+32
    print("The temperature in celsius is",celsius,".")