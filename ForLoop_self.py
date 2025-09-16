# Print numbers and strng values

# nums=[10,20,40,50,60]
# veggies=["Potato","Tomato","ladyfinger","Brinjal"]
# for val in nums:
#     print(val)

# for val in veggies:
#     print(val)


# Print tuple

# tup=(10,2,3,4,5,6,7,2,4,)
# for num in tup:
#     print(num)

# Print String characters

# str="Dharmendra"

# for char in str:
#     if(char=='m'):
#         print("M Found!!..")
#         break
    
# else:
#     print("Dadlani")


# Print the number using list using for loop
# num=[1,4,9,16,25,36,49,64,81,100]

# num=[1,4,9,16,25,36,49,64,81,100]


# for i in num:
#     print(i)


# Search number x in tuple

# num=(1,4,9,16,25,36,49,64,81,100,36)
# idx=0
# x=36

# for i in num:
#     if(i==x):
#         print("Number found at" ,idx)
#     idx+=1

# Range function in Loop

print(range(5))

seq=range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# print(seq[4])

# for i in seq:
#     print(i)


# for i in range(10):  # Range stop condition
#     print("Range values ",i)


# for i in range(2,10):  #start and stop condition
#     print(i)


# for i in  range(2,10,2): # start stop and step size
#     print(i)

# print odd and even numbers

# for i in range(1,100,2):
#     print(i)

# for i in range(2,100,2):
#     print(i)

#print numbers from 1 to 100

# for i in range(1,101):
#     print(i)


# print numbers from 100 to 1

# for i in range(100,0,-1):
#     print(i)


#print multiplication table

# n=int(input("Enter number : "))
# for i in range(1,11):
#     print(n, "x",  i, "=",  i*n)
    

#Pass when user dont want to write anything inside loop 

# for i in range(5):
#     #empty
#     pass

# if(i>5):
#     pass

# print("some Useful work")

#Make a sum of first n natural numbers

# n=int(input("Enter the Number : "))
# sum=0

# for i in range(1,n+1):
#     sum +=i
# print(sum)


# Write a program to find factorial of first n natural numbers
# ex n=5, 1x2x3x4x5

n=int(input("Enter the Number : "))
fact=1
i=1

while(i<=n):
    fact*=i
    i+=1
print("factorial of :",fact )
