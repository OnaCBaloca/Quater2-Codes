kwh= int(input("Enter  the number of kilowatt-hours used:"))
def tot_ele_bill(k):
   if k > 0 and k <= 100:
       return k*5
   elif k>= 101 and k<=200:
       return k*7
   elif k>= 201 and k<=500: 
       return k*10
   elif k>=500:
       return k*12
   else:
        print("Error")
a= tot_ele_bill(kwh)
ttbb= a + 50
print("Total Electricity Bill:$", ttbb)