#Question 3
# Using loop of your choice, WITI  has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89% Grade is   B
# 70% - 79% Grade is   C                                                        
# 60% - 69%  Grade is  D                  
# 50% - 59%  Grade is  E  
# < 50% Fail 

#ansers
mark =int(input("Enter the score:\t"))
if mark >=90 and mark <=100:
    print("Grade A")
elif mark >=80 and mark <=89:
    print("Grade B")
elif mark >=70 and mark <=79:
    print("Grade C")
elif mark >=60 and mark <=69:
    print("Grade D")
elif mark >=50 and mark <=59:
    print("Grand E")
else:
    print("fail")
