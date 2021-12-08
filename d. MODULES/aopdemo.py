#aopdemo.py ---- main program
from menu import menu
from aop import *

import sys

while(True):
    
    menu()  
    
    print("")
    choice = int(input("ENTER YOUR CHOICE : "))
    print("")
    
    if choice == 1 : 
        addop()
        break

    elif choice == 2 : 
        subop()
        break
        
    elif choice == 3 : 
        mulop()
        break
        
    elif choice == 4 : 
        divop()
        break
        
    elif choice == 5 : 
        modop()
        break
        
    elif choice == 6 : 
        expop()
        break
        
    elif choice == 7 :
        print("THANKS FOR USING THIS APPLICATION !")
        break  
        print("")
    else:
        print("")
        print("YOUR CHOICE OF OPERATION IS WRONG!!!")
        print("")