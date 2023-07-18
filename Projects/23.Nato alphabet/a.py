import pandas

alphabet=pandas.read_csv("nato_phonetic_alphabet.csv")

alph_dict={row.letter:row.code for (index, row) in alphabet.iterrows()}


name=input("State your name here: ").upper()

name_code={letter:code for char in name for (letter, code) in alph_dict.items() if char==letter}
print(name_code)