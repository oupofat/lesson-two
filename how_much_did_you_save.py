'''How Much Did You Save?
You have a coupon. If says if you buy $50.00 worth of products or more, you save 20%. If you buy less than $50.00 worth of products, you save %12.

Ask the user what is the amount of their purchase and tell them what's the new total after the coupon is applied, and also tell them how much they saved.'''

cost = float(input("how much did you spend?"))
if cost >= 50:
        saved = cost * .20
        total = (cost - saved)        
        print("this is your new total",total,".")
        print("this is how much you saved",saved,".")
else: 
        saved = cost * .12
        total = (cost - saved)        
        print("this is your new total",total,".")
        print("this is how much you saved",saved,".")