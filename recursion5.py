# Write a recursive function to print MySirG N times on the screen.
def nth(n):
    if n>0:
        print("my sir g")
        nth(n-1)

nth(3)