name = input("What is your first name?")
age = input("How old are you? ")
print("You are " + name + " and " + age + " years old")

weight = int(input("Weight: "))
unit = input("Kg or Pounds? Answer in 'K' or 'L'")
if unit == "k":
    print("Weight in kg: " + str(weight))
elif unit == "l":
    weight *= 2.2
    print("Weight in kg: " + str(weight))
else:
    print("Invalid Input. please try again")

# PROGRAM TO CALCULATE DIMENSIONS OF A CIRCLE
radius = float(input("Length of radius: "))
pi = 3.14
area = pi*radius**2
volume = 4/3 * pi * radius**2
print("The circle has an area of " + str(area) + " units")

# PROGRAM TO CALCULATE DIMENSIONS OF A SQUARE
side = float(input("Length of side: "))
area = side**2
print("The square has an area of " + str(area) + " units")

# PROGRAM TO CALCULATE DIMENSIONS OF A cube
length = float(input("Side length of cube: "))
area = 6*length**2
vol = length**3
print("The cube has an area of " + str(area) + " units")
print("The cube has a volume of " + str(vol) + " units cubed")

# PROGRAM TO CALCULATE DIMENSIONS OF A cuboid

l = float(input("Length of the cuboid: "))
b = float(input("Breadth of the cuboid: "))
h = float(input("Height of the cuboid: "))
area = 2*(l*b+b*h+l*h)
vol = l*b*h
print("The cuboid has an area of " + str(area) + " units squared")
print("The cuboid has a volume of " + str(vol) + " units cubed")

# PROGRAM TO CALCULATE SIMPLE AND COMPOUND INTEREST
pri_amt = float(input("Principal Amount: "))
yrs = float(input("Time period in years: "))
rate = float(input("Annual Interest rate:"))
si = (pri_amt * rate * yrs/100)
mature_si = pri_amt+si
ci = pri_amt*(1 + rate/100)**yrs - pri_amt
mature_ci = pri_amt + ci
print("-----------")
print("Simple Interest: " + str(si))
print("MAturity amount with Simple Interest: " + str(mature_si))
print("Compound Interest: " + str(ci))
print("MAturity amount with compound Interest: " + str(mature_ci))
