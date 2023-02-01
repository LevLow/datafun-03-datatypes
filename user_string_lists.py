"""
Name: Levi Lowther
Date: 1/31/23
Domain: Art
Let's make this arty and funny! 
"""


import random


list_artists = ["Vincent", "Pablo", "Salvidor", "Gustav", "Michelangelo", "Leonardo"]
list_verbs = ["painted", "sculpted", "drew", "carved"]
list_adjectives = ["many", "few", "beautiful", "unsightly", "tiny"]
list_colors = ["red", "green", "blue", "yellow", "orange", "purple"]
list_nouns = ["paintings", "sculptures", "carvings", "drawings"]

print()
print("String Lists 1. Using Python Built-in functions")
print()
word_count = len(list_artists)
print(f"Here are the number of artists we have to choose from: {word_count}")
print()
verb_set = set(list_verbs)
print(f"Here are the verbs we can choose from: {verb_set}")
print()
colors_nouns = tuple(zip(list_colors, list_nouns)) #without the tuple it won't print instead gives a zip object location 
print(f"Here is the tuple of colors and nouns: {colors_nouns}")
print()
print()


print()
print("String Lists 2. Random Choice")
print()
random_artist = random.choice(list_artists)
print(f"Here is a random artists from the list: {random_artist}")
print()
art_sentence = (
    f"{random.choice(list_artists)} {random.choice(list_verbs)} "
    f"{random.choice(list_adjectives)} {random.choice(list_colors)} {random.choice(list_nouns)}."
)
print(f"Here is a random, and probably factually incorrect, art sentence: {art_sentence}")
print()
print()

print()
print("String Lists 3. Get Unique Words")
print()
with open("text_hamlet.txt", "r") as fileObject:
    text = fileObject.read()
    list_words = text.split() 
    unique_words = set(list_words)
word_count = len(list_words)    
unique_word_ct = len(unique_words)

print(f"The number of words in Shakespear's play Hamlet is: {word_count}.")
print()
print(f"The number of unique words in Shakespear's play Hamlet is: {unique_word_ct}. I would say that is an impressive list of words!")
print()

