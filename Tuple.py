# Removing duplicate from Tuple 

t1=(1,2,2,3,1,4,5,4)

l1=set(t1)
l2=list(set(t1))   #this will convert into list
print(t1)
print(l2)


# Filter Tuple

t1=("dharm","","sandy","david","","Ankit")
print(t1)

l1=list(filter(None,t1))
print(l1)

# Map Tuple



# sort a tuple of tuples by 2nd item

# Count Elements

t1=(10,20,30,40,50)
t2=len(t1)
print("length of tuple is :: ",t2)


# Modify tuple
t1=(11,[22,33],44,55)
t2 = list(t1)
t2[1][0]=20
t2[1][1]=30
print(t2)
