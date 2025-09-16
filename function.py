
def greet(name):
    return "Hello " + name
print(greet("Dharam"))


def suqare(x):
    return x*x
print(suqare(4))

# Create function with length of argument
def arg(a,b,c):
    print(a,b,c)

arg(20,30,40)
    
# Create function with default argument

def detail(name='dharam',rno=234):
     print(name,rno)

detail()
detail("Test")
detail('test123',566)



# Create an inner function

def fun1(a,b): 
    print(a+b)
def fun2(): 
    fun1(10,5)
fun2()


