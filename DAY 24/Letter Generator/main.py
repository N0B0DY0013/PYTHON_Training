#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        

invited_names = []

with open("./Input/Names/invited_names.txt", mode = "r") as file_to_read:
    invited_names = file_to_read.readlines()

template_letter = ""

with open("./Input/Letters/starting_letter.txt", mode = "r") as file_to_read:
    template_letter = file_to_read.read()
    
for name in invited_names:
    name_to_write = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{name_to_write}.txt", mode = "w") as file_to_write:
        file_to_write.write(template_letter.replace("[name]", name_to_write))
