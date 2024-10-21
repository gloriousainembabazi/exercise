# Question 2(i)

# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category ="Normal weight"
    elif 25 <= bmi < 30:
        category ="Overweight"
    else:
        category ="Obese"
    
    return bmi, category

weight = 70  
height = 1.75  
bmi_value, bmi_category = calculate_bmi(weight, height)
print(f"BMI: {bmi_value:.2f}, Category: {bmi_category}")





# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)

#answers
import math
radius = int(input("Enter the radius of the cylider:"))
height =int(input("Enter the height of the cylinder:"))
pie = math.pi
volume = pie*radius**2*height
print(volume)