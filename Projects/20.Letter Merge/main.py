#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("C:\\Users\\a\\Desktop\\Python\\Projects\\20.Letter Merge\\Input\\Names\\invited_names.txt") as data:
    names=data.readlines()

with open("C:\\Users\\a\\Desktop\\Python\\Projects\\20.Letter Merge\\Input\\Letters\\starting_letter.txt") as data:
    letter_content=data.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_content.replace("[name]", stripped_name)
        with open(f"C:\\Users\\a\\Desktop\\Python\\Projects\\20.Letter Merge\\Output\\ReadyToSend\\{stripped_name}.txt", mode="w") as ready_letters:
            ready_letters.write(new_letter)
