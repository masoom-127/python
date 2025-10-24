#  Write a Python script to make a menu driven program in which user has to choose one of the options from four given options 1 Positive 2 Negative 3 Non-Positive 3 Simple Interest 4 And find roots of quadratic equation Match and execute appropriate code on user selection
a=int(input("chose nnumber 1to9 "))
match a:
    case 1 :
        s=int(input("enyer a number"))
        if s>0:
            print("postive")
        elif s<0:
            print("negetive")
        else :
            print("number is zero")
    case 3:
        print("enter p rand t")
        p,r,t=int(input("enetr a amount")),int(input("enetr a time")),int(input("enetr a  enetr interset"))
        si=(p*t*r)/100
        print(" interset",si)
    case 4:
        n=int(input("netr an number"))
        if n%2==0:
            print("even")
        else:
            print("odd")
    case 2:
      print("enter a value a b,c") 
      a,b,c=int(input()),int(input()),int(input())
      r1=(-b+(b*b-4*a*c)**0.5)/2*a
      r2=(-b-(b*b-4*a*c)**0.5)/2*a
      print("root are",r1,r2)
    case _:
        print("invalif choice")






