#divop.py
from excep import AkibDivisionError
def division(a,b):
    if(b==0):
        raise AkibDivisionError #here raise is used for hitting/generating the exception
    else:
        c=a/b
        return c
    
#here division(a,b) is comes under common function performing division of two value and hitting/generating the exception which was already developed.