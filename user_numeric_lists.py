"""
Name: Levi Lowther
Date: 1/31/2023
Domain: Art

"""

# import some modules first - how many can you make use of?

import math
import statistics as stats


# define some functions


def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

# Create some lists
# list1 will be the age of artists at thier deaths
list1 = [ 47, 46, 44, 42, 43, 39, 37, 37, 37, 37, 36, 36, 36, 35, 33, 33, 32, 26, 67, 54, 51, 69, 61, 57, 44, 49, 47, 42, 39, 56, 61, ]
# Theses lists will represent the hours of operation of an art museaum
# and the number of visitors per hour.  
listx_operating_hours = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
listy_number_visitors = [ 5, 6, 8, 7, 9, 10, 8, 11, 9, 12,  ]
print()



print("List 1. List Statistics")
print()
mean = stats.mean(list1)
median = stats.median(list1)
mode = stats.mode(list1)
print(f"The mean age at which these artists died is {mean:.2f}.")
print(f"The median age at which these artist died is {median}.")
print(f"The most common age at which these artists died is {mode}.")
print()
stdev = stats.stdev(list1)
variance = stats.variance(list1)
print(f"The standard deviation in age is {stdev:.2f}.")
print(f"The variance across ages is {variance:.2f}.")
print()
print()



print("List 2. Lists - Correlation and Prediciton")
print()
correlationxy = stats.correlation(listx_operating_hours, listy_number_visitors)
slope, intercept = stats.linear_regression(listx_operating_hours, listy_number_visitors)
print(f"The correlation between open hours and visitors is {correlationxy:.2f}.")
print(f"The slope is {slope:.2f} and the intercept is {intercept:.2f}.")
print()
newx = 15
newy = slope * newx + intercept
print(f"If the museum were to remain open for 15 hours, the projected number of visitors is {newy:.2f} ")
print()
print()



print("Lists 3. Lists - Using Python Built-in Functions")
print()
max = max(list1)
min = min(list1)
len = len(list1)
sum = sum(list1)
avg = sum / len
set1 = set(("museum", "visitor", "artist"))
asc_ages = sorted(list1)
desc_ages = sorted(list1, reverse=True)
print(f"The maximum age of death was {max}.")
print(f"The minimum age of death was {min}.")
print(f"The number of ages in the list is {len}.")
print(f"The sum of all the ages is {sum}.")
print(f"The average of the ages is {avg:.2f}.")
print(f"The maximum age of death was {max}.")
print(f"My domain inculdes things like {set1}.")
print()
print(f"Here are the ages in ascending order: {asc_ages}.")
print()
print(f"Here are the ages in descending order: {desc_ages}.")
print()
print()



print("List 4. List Methods")
print()
lst = [ 2, 3, 4, 5, 6, ]
print(f"First we have a list: {lst}.")
print()
lst.append(7)
print(f"Now we add 7 to the end: {lst}.")
print()
lst.extend([8, 9, 10,])
print(f"And now we extend the list with 8, 9, and 10: {lst}.")
print()
i = 0
firstvalue = 1
lst.insert(i, firstvalue)
print(f"Now we add the first value: {lst}.")
print()
number_to_remove = 7
lst.remove(number_to_remove)
print(f"Now we remove 7 from the list: {lst}.")
print()
ct_of_2 = lst.count(2)
print(f"We can count how many times the number 2 appears in the list: {ct_of_2}.")
print()
asc_lst = lst.sort()
print(f"Here is the ascending list: {lst}.")
print()
desc_lst = lst.sort(reverse=True)
print(f"Here is the descending list: {lst}.")
print()
new_lst = lst.copy()
print(f"Here is a new copy of the list: {new_lst}.")
print()
first_pop = new_lst.pop(0)
print(f"We used the pop command to remove the first item: {new_lst}.")
print()
last_pop = new_lst.pop(-1)
print(f"We used the pop command to remove the last item: {new_lst}.")
print()
print()


print("List 5. List Transformations - Using filter() and map()")
print()
ages_under_40 = list(filter(lambda x: x < 40, list1))
print(list(ages_under_40))
print(f"Here is our list of ages only keeping ages under 40: {ages_under_40}")
print()
cbrt_list1 = list(map(lambda x:(x ** (1/3)), list1))
print(f" The cube roots of all the ages in our list are: {cbrt_list1} ")
""" having and issue here printing the cube roots with rounded decimal places. 
to print I have to make it a list, which makes it so that I can't round the numbers.
must research further."""
print()
# Say "map r to pi r squared" and cast to a list
volume_list = list((map(lambda r: r * r * r, list1)))
print(f"If each age were the length of the side of a cube the volume of each would be: {volume_list}")
print()
print()



print("Lists 6. List Transformations - Using List Comprehension")
print()
ages_over_35 = [x for x in list1 if x > 35]
print(f"Here are the ages over 35 using comprehension {ages_over_35}")
print()
triple_age = [x * 3 for x in list1]
print(f"If our artists had lived three times as long, these would have been their ages of death {triple_age}")
print()
cube_age = [x ** 3 for x in list1]
print(f"Here are the ages if they were cubed: {cube_age}")
print()

#I had the most issues with attempting to print each different itteration to show the changes I was making. I figured out 
#a way. But I am unsure if it was what I was supposed to do.



