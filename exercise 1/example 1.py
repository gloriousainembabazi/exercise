#question 1(i)
#Temperature classiffer: using a fuction ,write a python script that takes
#a temperature as input and classifies it into the following categories:
# below 0 degrees celicius: freezing
# 0 to 10 degrees celicius :cold
#11 to 20 degrees celicius:moderate
# 21 to 30°C: Warm 
# Above 30°C: Hot 

def classify_temperature(temp):
    if temp < 0:
        print("freezing")
    elif 0 <= temp <= 10:
        print ("cold")
    elif 11 <= temp <= 20:
        print("Warm")
    elif 21 <= temp <= 30:
        print("moderate")
    else:
        print("Hot")

try:
    temperature = float(input("Enter the temperature in degrees Celsius: "))
    classification = classify_temperature(temperature)
    print(f"The temperature is classified as: {classification}")
except ValueError:
    print("Please enter a valid number.")
temperature=float(input("Enter "))







# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and provide the answer in 1 decimal place

#aswers
import math

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return round(volume, 1)

radius_input = float(input("Enter the radius of the sphere: "))
volume = calculate_sphere_volume(radius_input)

print(f"The volume of the sphere with radius {radius_input} is {volume} cubic units.")