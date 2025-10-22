#Function
def kdr(k,r):
    fee= k*r
    return fee


#Main Program
kilom= int(input("Enter distance in kilometer:"))
ratek= int(input("Enter rate per kilometer (₱):"))

feez= kdr(kilom, ratek)

print("Total Delivery Fee: ₱",feez)