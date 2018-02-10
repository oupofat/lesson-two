'''Price of the ride
A carnival ride costs $12.00 for adults; $6 for kids (12 or under); $7 for senior citizens (60 or older). You have to be at least 48 inches to ride.

Write a program to ask the user for their age and then their height. If they qualify to ride, tell them the cost of their ride. If they do not qualify to ride, tell them that they cannot ride.'''

age = input("How old are you?(age)")
height = input("How tall are you? (height)")

if height <="48":
    print ("You are to short!")
elif age >= "60":
    print ("Your cost is $7.00.")
elif age <="12":
    Print ("Your cost is $6.00.")
else:
    print ("Your cost is $12.00.")