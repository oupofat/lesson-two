'''Bonus: Buffet
There is a buffet my family likes called Tokyo Bay. It charges $15.00 per adult and $10.00 per child. On Tuesdays, though, kids eat free.

Write a program to ask the user:

How many adults are in their family?
How many children are in their family?
What day of the week is it?
Tell the user how much it will cost for the family to eat at Tokyo Bay.'''

adults = int(input("How many adults?"))
kids = int(input("How many kids?"))
day = input ("Is it tuesday(y or n)")
adults = adults * 15
kids = kids * 10
if day == "y": 
    total_sum = adults
    print ("Your total cost with out adding the kids is", total_sum,".")
else: 
    total_sum = adults + kids
    print ("Your total cost is", total_sum,".")