
# # Remove empty string from list

# list1=["dharm","","sandy","david","","Ankit"]
# print(list1)


# l1=list(filter(None,list1))
# print(l1)



# Remove duplicates from list

# d1=[1,2,2,3,1,4,5,4]

# l1=set(d1)
# l2=list(set(d1))   #this will convert into list
# print(l1)
# print(l2)


# Remove all occurence of specific item from list 
list1=[5,20,15,20,25,50,20]



#list comprehension for numbers
# l1=[1,2,3,"Jess",4,5,"kelly","john",6]
# expected=[1,2,3,4,5,6]
# for string use str
# l1=[1,2,3,"Jess",4,5.5,"kelly","john",6]

# numbers=[i for i in l1 if isinstance(i,(int,float))]
# print(numbers)



# list_of_list =[[1,2],[3,4],[5,6,7]]
# output=[1,2,3,4,5,6,7]

# l1=[[1,2],[3,4],[5,6,7]]

# l2=[item for sublist in l1 for item in sublist]
# print(l2)

# Concatdnate two lists index wise
# list1=["M","na","i","Ke"]
# list2=["y","me","s","lly"]

# list3=[i+j for i,j in zip(list1,list2)]
# print(list3)


#
# list1=["Hello","take"]
# list1=["Dear","Sir"]

# output=["Hello Dear","Hello Sir","take Dear","take sir"]

# list1=["Hello ","take "]
# list2=["Dear","Sir"]

# list3=[x + y for x in list1 for y in list2]
# print(list3)


# Iterate both list simulataniously
# list1=[10,30,30,40]
# list2=[100,200,300,400]

# Expected output
# 10  400
# 20  300
# 30  200
# 40  100

# list1=[10,20,30,40]
# list2=[100,200,300,400]

# for x,y in zip(list1,list2[::-1]):
#     print(x,y)


# Add new item to list after specified item


# list1=["dharam","dadlani"]


# list1.append("test")
# print(list1)



# # Extend list by adding sublist
# list1=['a','b'["c",['d','e',['f','g'],'k'],'i'],'m','n']
# sublist=['h','i','j']
# Expected Results= ['a','b'["c",['d','e',['f','g','h','i','j'],'k'],'i'],'m','n']

# list1=['a','b',['c',['d','e',['f','g'],'k'],'i'],'m','n']
# sublist=['h','i','j']

# list1[2][1][2].extend(sublist)
# print(list1)

#Replace list item with new value if found (need to check it)
# list1=["dharam","Test"]

# list1[1]=("Dadlani")
# print(list1)