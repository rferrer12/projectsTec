F=float(input("Please insert temperature in Fahrenheit "))
C= 5*(F-32)/9
print(F, " degrees Fahrenheit are equal to ", C, " degrees Celcius")
if(C<100):
    print("Water will not boil at this temperature")
else:
    print("Water will boil at this temperature")
