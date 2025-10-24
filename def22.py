# Write a Python function to count frequency of each element of the list and store list elements in the dict object as keys and element frequency as data values.
 
def repetion(mylist):
   d1={}
   i=0
   while i <len(mylist):
      if mylist.index(mylist[i])==i:
         f=mylist.count(mylist[i])
         d1[mylist[i]]=f

      i+=1
   return d1



l=[3,4,5,5,6,74.4,4,5]
repetion(l)
