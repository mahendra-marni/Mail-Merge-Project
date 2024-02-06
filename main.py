with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as content_file:
    content = content_file.read()
    for name in names:
        x = content.replace("[name]", name.strip())

        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
            file.write(x)




