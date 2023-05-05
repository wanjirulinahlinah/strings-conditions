



























class Student:
    school = "Akirachix"
    def __init__(self,age,school,nationality,first_name,last_name,country,name):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.name = name
        self.age = age
        self.school = school
        self.nationality=nationality
    def greet_Student(self):
        return f"Hello {self.name},welcome to {self.school},proudly {self.nationality}"
    # question1
    def show_full_name(self):
        return f"Hello {self.first_name} {self.last_name}"
    def year_of_birth(self):
        return f"{2023-self.age}"
    def show_initials(self):
        return f"{self.first_name[0]},{self.last_name[0]}"
    
    
    # Control Flow
    def even_numbers():
    x=range(10)
    for i in x:
        if i%2==0:
            print(i)

def odd_numbers():
    x=range(10)
    for i in x:
        if i in x:
            if i%1==0:
                print(i)  

def divisible_by_five():
    x=range(30)
    for i in x:
        if 1%5==0:
             print(f"{i}is divisible by 5")  
        else:
            print(f"{i}is  not divisible by 5")  


def multiple_comparisons():
    x=range(30)
    for i in x:
        if i%2==0:
            print(f"{i}is  divisible by 2") 
        elif i%2==0:
                 print(f"{i}is  divisible by 3") 
        elif i%2==0:
                    print(f"{i}is  divisible by 5") 
        else:
                         print(f"{i}is  divisible by 2,3 or 5") 

def divisible_by_two_and_three():
     x=range(30)
     for i in x:
         if i%2==0 and i%3==0:
            print(f"{i}is  divisible by both 2 and 3")
         elif i%2==0 and i%3==0:
                 print(f"{i}is  divisible by either 2 or 3")
         if i%2==0 and i%3==0:
                     print(f"{i}is  divisible by 2 or 3")  

def while_loop():
    x=1
    while x<10:
        print(x)
        x+=1



def break_statement():
    x=1
    while x<10:
        print(x)
        if x==5:
            break_statement
            x+1

def continue_statement():
    x=1
    while x<10:
        x+=1
        if x%2!=0:
            continue
        print(x)                





# arguments
def my_country(country="Rwanda"):
    print(f"Hello from {country}")

    def great(*names):
        for name in names:
            print(f"Hello {name}")
def sum(*numbers):
    output=0
    for number in numbers:
        output+=number
    return output
def multiplication(*nambari):
    answer=1
    for namb in nambari:
        answer*=namb
    return answer
def student_att(**kwags):
    for key,value in kwags.items():
        print(f"{key}:{value}")
def concatenate_args(*argss):
    strs=""
    for arg in argss:
        strs+=arg
    return strs
def concatenate_kwargs(**kwargs):
    answer = ""
    for key,value in kwargs.items():
        answer+=value
    return answer


def even_numbers():
    n = 0
    while n < 50:
        n += 1
        if n % 2 == 0:
                continue
        print(n)
        
# Assignments operators
# Write a function that takes an integer argument and prints "Prime" if the number is prime, 
# and "Not prime" if the number is not prime.  
def intergers():
    x=range(30)
    for i in x:
        if i%2!=0:
            print(f"{i}is a prime number")
        else:
            print(f"{i}is not a prime number")


# Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.

def list_of_integers():
    x=range(40)
    sums = 0
    for i in List:
        if i % 2 == 0 : 
            sums += i
            print(sums)

#  Write a function that takes any two integers as input, and prints the sum of all the numbers
#  between the two integers (inclusive) that are divisible by 3
def integers():
    for i in range(1, m+1):
        sum1 =0
        sum2 =0
        if i % n ==0:
            sum1 += i
        else:
            sum2 +=i
            print(f"{sum1} and {sum2}")
            
            # Hello
            
            
            def hello(name):
     print(f"Hello {name}")

def greet(*names):
     for name in names:
        print(f"Hello {name}")


def greet():
    print('Hello world')


# math

def greet():
    print('Hello World')

def add(a,b):
    answer=a +b
    return answer

def add(a,b):
    answer = a+b
    return answer

def subtract(d,e):
    answer = d - e
    return answer

def divide(m,k):
    answer = m / k
    return answer

def mutiply(n,l):
    answer = n*l
    return answer 

def reminder(p,l):
    answer = p % l
    return answer 

# student
def year_of_birth(name, age):
    year = 2023 - age
    print(f"Hello {name} you were born in  {year}")
        

                

