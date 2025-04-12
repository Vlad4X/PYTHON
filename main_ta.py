"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Vladimir Dedek
email: vladimir.dedek.mx@gmail.com
"""
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("username: ")
password = input("password: ")

if users.get(username) == password:
    print("-" * 40)
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print("-" * 40)
else:
    print("unregistered user, terminating the program..")
    exit()

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]


selection = input("Enter a number btw. 1 and 3 to select: ")

if not selection.isdigit() or int(selection) not in [1, 2, 3]:
    print("Invalid input, terminating the program..")
    exit()

text = TEXTS[int(selection) - 1]
print("-" * 40)

import string

words = text.split()
clean_words = [word.strip(string.punctuation) for word in words]

word_count =len(clean_words)
titlecase_count = sum(1 for word in clean_words if word.istitle())
uppercase_count = sum(1 for word in clean_words if word.isupper()
                       and word.isalpha())
lowercase_count = sum(1 for word in clean_words if word.islower())
numeric_count = sum(1 for word in clean_words if word.isdigit())
numeric_sum = sum(int(word) for word in clean_words if word.isdigit())

print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}")
print("-" * 40)

word_lengths = {}
for word in clean_words:
    length = len(word)
    word_lengths[length] = word_lengths.get(length, 0) + 1

sorted_lengths = sorted(word_lengths.items())

print("LEN| OCCURENCES |NR.")
print("-" * 40)

for length, count in sorted_lengths:
    print(f"{length:3}| {"*" * count:<17} | {count:<5}")
 

