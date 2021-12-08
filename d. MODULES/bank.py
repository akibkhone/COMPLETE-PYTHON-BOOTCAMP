def Simpleinterest():

      p = float(input("Enter Principle Amount : "))
      t = float(input("Enter Time : "))
      r = float(input("Enter Rate Of Interest : "))
    
      si = (p*t*r)/100
      tamt = p+si

      print("Simple Interest Result ")
      print (f"Principle Amount : {p}")
      print (f"Rate Of Interest : {r}")
      print (f"Simple Interest : {si}")
      print (f"total Amount To Pay : {tamt}")
              
              
    
    