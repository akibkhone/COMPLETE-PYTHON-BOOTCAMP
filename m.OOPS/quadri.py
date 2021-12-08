class quad:
    
    def readvalues(self):
        self.a=float(input("Enter Value Of a : "))
        self.b=float(input("Enter Value Of b : "))
        self.c=float(input("Enter Value Of c : "))
      
    def calroots(self):  
        self.r1=(- self.b + ( (self.b**2 - 4 * self.a * self.c)**0.5 )) / ( 2 * self.a)
        self.r2=(- self.b - ( (self.b**2 - 4 * self.a * self.c)**0.5 )) / ( 2 * self.a)
    
    def displayresult(self):
        print(f"Value Of a = {self.a}")
        print(f"Value Of b = {self.b}")
        print(f"Value Of c = {self.c}")
        print(f"ROOT 1 = {self.r1}")
        print(f"ROOT 2 = {self.r2}")
        
#MAIN PROGRAM

qo=quad()
qo.readvalues()
qo.calroots()
qo.displayresult()