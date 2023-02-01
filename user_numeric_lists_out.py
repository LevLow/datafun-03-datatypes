(base) PS C:\Users\levil\Documents\datafun-03-datatypes> & C:/Users/levil/AppData/Local/Programs/Python/Python310/python.exe c:/Users/levil/Documents/datafun-03-datatypes/user_numeric_lists.py

List 1. List Statistics

The mean age at which these artists died is 44.29.
The median age at which these artist died is 42.
The most common age at which these artists died is 37.

The standard deviation in age is 10.76.
The variance across ages is 115.88.


List 2. Lists - Correlation and Prediciton

The correlation between open hours and visitors is 0.87.
The slope is 0.62 and the intercept is 5.07.

If the museum were to remain open for 15 hours, the projected number of visitors is 14.43


Lists 3. Lists - Using Python Built-in Functions

The maximum age of death was 69.
The minimum age of death was 26.
The number of ages in the list is 31.
The sum of all the ages is 1373.
The average of the ages is 44.29.
The maximum age of death was 69.
My domain inculdes things like {'visitor', 'artist', 'museum'}.

Here are the ages in ascending order: [26, 32, 33, 33, 35, 36, 36, 36, 37, 37, 37, 37, 39, 39, 42, 42, 43, 44, 44, 46, 47, 47, 49, 51, 54, 56, 57, 61, 61, 67, 69].

Here are the ages in descending order: [69, 67, 61, 61, 57, 56, 54, 51, 49, 47, 47, 46, 44, 44, 43, 42, 42, 39, 39, 37, 37, 37, 37, 36, 36, 36, 35, 33, 33, 32, 26].


List 4. List Methods

First we have a list: [2, 3, 4, 5, 6].

Now we add 7 to the end: [2, 3, 4, 5, 6, 7].

And now we extend the list with 8, 9, and 10: [2, 3, 4, 5, 6, 7, 8, 9, 10].

Now we add the first value: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

Now we remove 7 from the list: [1, 2, 3, 4, 5, 6, 8, 9, 10].

We can count how many times the number 2 appears in the list: 1.

Here is the ascending list: [1, 2, 3, 4, 5, 6, 8, 9, 10].

Here is the descending list: [10, 9, 8, 6, 5, 4, 3, 2, 1].

Here is a new copy of the list: [10, 9, 8, 6, 5, 4, 3, 2, 1].

We used the pop command to remove the first item: [9, 8, 6, 5, 4, 3, 2, 1].

We used the pop command to remove the last item: [9, 8, 6, 5, 4, 3, 2].


List 5. List Transformations - Using filter() and map()

[39, 37, 37, 37, 37, 36, 36, 36, 35, 33, 33, 32, 26, 39]
Here is our list of ages only keeping ages under 40: [39, 37, 37, 37, 37, 36, 36, 36, 35, 33, 33, 32, 26, 39]

 The cube roots of all the ages in our list are: [3.6088260801386944, 3.583047871015946, 3.530348335326063, 3.4760266448864496, 3.503398060386724, 3.3912114430141664, 3.332221851645953, 3.332221851645953, 3.332221851645953, 3.332221851645953, 3.3019272488946263, 3.3019272488946263, 3.3019272488946263, 3.2710663101885897, 3.207534329995826, 3.207534329995826, 3.1748021039363987, 2.9624960684073702, 4.0615481004456795, 3.7797631496846193, 3.708429769266189, 4.101565929702347, 3.9364971831021727, 3.8485011312768047, 3.530348335326063, 3.6593057100229713, 3.6088260801386944, 3.4760266448864496, 3.3912114430141664, 3.825862365544778, 3.9364971831021727]

If each age were the length of the side of a cube the volume of each would be: [103823, 97336, 85184, 74088, 79507, 59319, 50653, 50653, 50653, 50653, 46656, 46656, 46656, 42875, 35937, 35937, 32768, 17576, 300763, 157464, 132651, 328509, 226981, 185193, 85184, 117649, 103823, 74088, 59319, 175616, 226981]


Lists 6. List Transformations - Using List Comprehension

Here are the ages over 35 using comprehension [47, 46, 44, 42, 43, 39, 37, 37, 37, 37, 36, 36, 36, 67, 54, 51, 69, 61, 57, 44, 49, 47, 42, 39, 56, 61]        

If our artists had lived three times as long, these would have been their ages of death [141, 138, 132, 126, 129, 117, 111, 111, 111, 111, 108, 108, 108, 105, 99, 99, 96, 78, 201, 162, 153, 207, 183, 171, 132, 147, 141, 126, 117, 168, 183]

Here are the ages if they were cubed: [103823, 97336, 85184, 74088, 79507, 59319, 50653, 50653, 50653, 50653, 46656, 46656, 46656, 42875, 35937, 35937, 32768, 17576, 300763, 157464, 132651, 328509, 226981, 185193, 85184, 117649, 103823, 74088, 59319, 175616, 226981]

(base) PS C:\Users\levil\Documents\datafun-03-datatypes> 