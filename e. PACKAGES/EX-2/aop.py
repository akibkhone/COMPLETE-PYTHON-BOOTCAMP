#aop.py 

from menu import menu

def readvalues(op):
    
    a=float(input(f"Enter First Value {op} : "))
    b=float(input(f"Enter Second Value For {op} : ")) 
    return a,b
    
def addop():  
    a,b = readvalues("Addition")
    print(f"Addition of {a} and {b} is : {a+b}")
    print('')
    
def subop():
    a,b = readvalues("Substraction")  
    print(f"Substraction of {a} and {b} is : {a-b}")
    print('')
    
def mulop():
    a,b = readvalues("Multiplication")
    print(f" Multiplication of {a} and {b} is : {a*b}")
    print('')
    
def divop():
    a,b = readvalues("Division")
    print(f"Division of {a} and {b} is : {a//b}")
    print('')
    
def modop():
    a,b = readvalues("Modulo Division")
    print(f"Modulo Division  of {a} and {b} is : {a%b}")
    print('')
    
def expop():
    a=float(input(f"Enter First Value for Base : "))
    b=float(input(f"Enter Second Value For Power : ")) 
    print(f"Exponentiation of {a} and {b} is : {a**b}")
    print('')
    