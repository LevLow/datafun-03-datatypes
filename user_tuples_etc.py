"""
Name: Levi Lowther
Date: 1/31/23
Domain: Art

"""


print("Task 5. Tuples and More")

tupleArt_weight = (10, 15, 17, 20)
tupleArt_volume = (4, 10, 18, 6)

tupleBoth = tupleArt_weight + tupleArt_volume

tupleweight_double = tupleArt_volume * 2


print(f"{tupleArt_weight = }")
print(f"{tupleArt_volume = }")
print(f"{tupleBoth = }")
print(f"{tupleweight_double = }")

hasSix = 6 in tupleArt_volume  # True
hasFour = 4 in tupleArt_weight  # False
print(f"Does volume contain the number six: {hasSix}")
print(f"Does weight contain the number four: {hasFour}")
print()
print()

print("Sets with Unions and Intersections")
setArt = {10, 20, 33, 40, 50}
setBrush = {70, 80, 33, 100, 120}

setCanvas = setArt | setBrush

setDraw = setArt & setBrush

print(f" The untion of sets Art and Brush is: {setCanvas}.")
print()
print(f" The intersection of sets Art and Brush is: {setDraw}.")
print()




print("Building a dictionary!")

with open("text_juliuscaesar.txt") as file_object:
    word_list = file_object.read().split()
word_counts_dict = {word: word_list.count(word) for word in word_list}

print(word_counts_dict)




