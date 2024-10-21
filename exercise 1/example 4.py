
#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.

# answers
favorite_foods =["Rice","chips","chicken","matooke", "posh"]
print(favorite_foods)
favorite_foods.append("cassava")
favorite_foods.append("Sweet potatoes")
print(favorite_foods)

favorite_foods.remove("Rice")
print(favorite_foods)






#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.

#aswers

numbers = [2, 5, 8, 10, 3, 6]

first_element = numbers[0]
last_element = numbers[-1]
print("First element:", first_element)
print("Last element:", last_element)
reversed_numbers = numbers[::-1]
print("Reversed list:", reversed_numbers)

total_sum = sum(numbers)
print("Sum of all elements:", total_sum)