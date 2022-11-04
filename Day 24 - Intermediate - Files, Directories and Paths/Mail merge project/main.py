# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt

PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()  # creates a list using each line as a list item

with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    letter = starting_letter.read()

for name in name_list:
    stripped_name = name.strip()
    # Replace the [name] placeholder with the actual name
    addressed_letter = letter.replace(PLACEHOLDER, stripped_name)

    # Save the letters in the folder "ReadyToSend"
    with open(f"Output/ReadyToSend/{stripped_name}'s letter.txt", mode="w") as finished_letter:
        finished_letter.write(addressed_letter)
