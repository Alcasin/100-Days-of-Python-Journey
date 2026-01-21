# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt") as file:
    names = file.read().splitlines()
    # print(names)

for name in names:
    with open("Input/Letters/starting_letter.txt") as file:
        letter = file.read()

    letter = letter.replace("[name]",name)
    print(name)
    print(letter)
    with open(f"Output/ReadyToSend/{name}.txt",mode = "w" ) as file:
        file.write(letter)


# with open("../../../../my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#Append
# with open("my_file.txt", mode="a") as file:
#     file.write("\n:))")

#Write
# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")
