import random

print("This programme will help you create a password using two words of your choice.")

word1 = input("Enter your first word: ").lower()
word2 = input("Enter your second word: ").lower()
words = [word1, word2]
characters = [".", ",", "!", "?", "-", "+", "_", ":", "(", ")", "[", "]", "{", "}", "@", "%", "#", "^"]
numbers = range(11)

password_contents = []
password = ""

chosen_word = random.choice(words)
letters_to_cap = random.sample(chosen_word, 2)
changed_word = ("".join([char.upper() if char in letters_to_cap else char.lower() for char in chosen_word]))

for i in words:
    if i == chosen_word:
        continue
    else:
        password_contents = [i, changed_word]

password_contents = password_contents + [random.choice(characters)] + [str(random.choice(numbers))]

def generate_password():
    random.shuffle(password_contents)
    global password
    for i in password_contents:
        password += i 
    return password

print(generate_password())
