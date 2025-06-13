# Open the file containing all the names of people to invite
all_names = open("./Input/Names/invited_names.txt")

# Open and read the starting letter template
with open('./Input/Letters/start_letter.txt') as letter:
    letter = letter.read()

# Loop through each name in the names file
for name in all_names:
    # Remove any leading/trailing whitespace or newline characters from the name
    stripped_name = name.strip()

    # Replace the placeholder [name] in the letter with the actual name
    replaced_letter = letter.replace('[name]', stripped_name)

    # Create a new personalized letter file for the current name
    with open(f"./Output/ReadyToSend/letter_{stripped_name}.txt", 'w') as new_letter:
        new_letter.write(replaced_letter)
