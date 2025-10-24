#create code detail about plyer like name century,50,more on using dict
n=int(input("how many player data tou want to strode name of player"))
players={}
for i in range(1,n+1):
    name=input("enter a player name")
    print("enter number of matches plyer ")
    a=input()
    print(" a total run")
    b=int()
    print(" a half centuries")
    c=int()
    print(" centuries")
    d=int()
    players[name]=(a,b,c,d)
for i,v in players.items():
    print(i,v)