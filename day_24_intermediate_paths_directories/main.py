PLACEHOLDER = "[name]"  # constants in python


with open("./Input/Names/invited_names.txt") as names_list:
  names = names_list.readlines()

with open("./Input/Letters/starting_letter.txt") as letters:
  letter_contents = letters.read()

  for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
    print(new_letter)

    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
      completed_letter.write(new_letter)
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp