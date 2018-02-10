'''Too Short to Ride
Ask the user to enter their height in inches (remember to convert it to an integer). If they are 48 inches or more, print "Go to go". Otherwise, print "You are too short to ride".'''

height = int(input("How tall are you?"))
if height >= 48:
    print("Go to go!")
else:
    print("You are to short to ride!")