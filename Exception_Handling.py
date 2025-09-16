

# try:

#     x=  10 /  0
# except  ZeroDivisionError:

#     print("Division By Zero!")



try:
    x=  10 /  2

except  ZeroDivisionError:
     print("Can not divide by zero!")
else:
     print("Division successful")
finally:
     print("This will execute finally")
