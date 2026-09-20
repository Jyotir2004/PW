def fibonacci(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def facto(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def add(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def even():
    l = []
    i = 0
    while i <= 100:
        if i % 2 == 0:
            l.append(i)
        i += 1
    return l


def odd():
    l = []
    i = 0
    while i <= 100:
        if i % 2 != 0:
            l.append(i)
        i += 1
    return l


def table(n):
    l = []
    i = 0
    while i <= 10:
        l.append(n * i)
        i += 1
    return l

def caheck_prime(n):
    i=0
    count=0

    while i<=n:
        if i%n==0:
            count+=1
        i+=1

    if count==2:
        return "prime"
    elif n>1:
        return "composite"
    else:
        return "non prime"



def display_num():
    sum=0
    l=[]
    i=0
    while i<=10:
        l.append(i)
        sum+=i
        i+=1
        l.append(sum)
    s=sum
    average=sum/10
    l.append(average)

    return l
 





def display_even():
    l=[]
    i=0
    while i<=10:
        if i%2==0:
            l.append(i)
        i+=1

    return l



def display_odd():
    l=[]
    i=0
    while i<=10:
        if i%2!=0:
            l.append(i)
        i+=1
    return l



def display_century():
    l=[]
    i=0
    while i<=100:
        l.append(i)
        i+=1
    return l


def table_of(n):
    l=[]
    for i in range(1,11):
        l.append(n*i)
    return l

def even_odd(n):
     if n%2==0:
        return "even"
     else:
        return "odd"

def cube_n(n):
    return n**3


def square_n(n):
    return n**2


def call_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact


def primine(n):
    i=0
    count=0
    while i<=n:
        if i%n==0:
            count+=1
        i+=1
    if count==2:
        return "prime"
    elif n>1:
        return "composite"
    else:
        return "non prime"


def fibo(n):
    if n==0 or n==1:
        return n
    return fibo(n-1)+fibo(n-2)


def dis():
    sum=0
    l=[]
    i=0
    while i<=10:
        l.append(i)
        i+=1
        sum+=i
        p=sum
        average=sum/10
        l.append(p)
        l.append(average)
    return l
        


def dio():
    l=[]
    sum=0
    i=1
    while i<=10:
        if i%2==0:
            l.append(i)
            sum+=i
            l.append(sum)
           
        i+=1
    return l
            
    



def deso():
    sum=0
    l=[]
    i=0
    while i<=10:
        if i%2!=0:
            l.append(i)
            sum+=i
            l.append(sum)
        i+=1
    return l

          
def oss():
   l=[]
   i=0
   while i<=100:
     if i%2!=0:
        l.append(i)
     i+=1
   return l


def evss():
    l=[]
    i=0
    while i<=100:
        if i%2==0:
            l.append(i)
        i+=1
    return l








            


