from art import logo
from art import alphabet
print(logo)
def cesar(text, shift, direction):
    new_text=""
    shift = (shift*-1) if direction == "decode" else shift
    for letter in text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=(position+shift)%26
            new_text+=alphabet[new_position]
        else:
            new_text += letter
    print(f"This is the {direction}d text: {new_text}")

def start():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()

    while not text[0].isalpha():
        print("You Should Only Write Letters!")
        text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    cesar(text, shift, direction)


start()
question=input("Start Again? y/n: ")


while question=="y":
    start()
    question=input("Start Again? y/n: ")