##write python function cal find id leapyear
def leap(year):
    if year%100==0:
        if year%400==0:
            return True
    else:
        if year%4==0:
            return True
        else :
            return False
