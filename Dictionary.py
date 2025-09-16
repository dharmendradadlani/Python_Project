
person={"name": "Dharam", "age":32}
print(person['name'])


#Delete list of keys from dictionary

dic1={"name":"dharam", "age": "30", "salary": "10000"}
d2=["name","salary"]
for i in d2:
    dic1.pop(i)
    print(dic1)

# check value is present in dictionary or not

d1={'one':1,'two':2,'three':3}
if 2 in d1.values():
    print("present")
else:
    print("not present")

# # Rename key of dictionary replace city with location
d1={"name":"dharam", "age": "30", "salary": "10000",'city':'Ahmedadabad'}


d1["Location"]=d1.pop("city")
print(d1)


# Get key of minimum value
d1={'one':1,'two':2,'three':3}
print(min(d1,key=d1.get))



