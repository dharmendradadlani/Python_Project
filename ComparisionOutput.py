#  Write a program to check whether you are eligible to vote or not
age=20

if age>=18:
    print("You are eligible to Vote")
else:
    print("You are not eligble to vote")


# eligiblity criteria for Marriage

age =21

if age>=21:
    print("You are eligible for Marriage")
else:
    print("you are not eligible for Marriage")


# Write a program wheather you are eligible for vote and Marriage or not
    
age=15

if age>=18 and age>=21:
    print("You are eligible for both")
elif age>=18 and age<=21:
    print("You are eligible for Vote but not for Marriage")

else:
    print("You are not eligble for both")
