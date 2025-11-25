D= int(input("Enter Distance in kilometers:"))
F= int(input("Enter fuel consumed in liters:"))

def fuel_eff(d,f):
    return d/f
a= fuel_eff(D,F)
print("Fuel Efficiency:", a,"km/L")