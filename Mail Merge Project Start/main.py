
list_of_invited = []
with open("Input/Names/invited_names.txt") as file:
    for name in file:
        list_of_invited.append(name.strip("\n"))
print(list_of_invited)
with open("Input/Letters/starting_letter.txt") as letter:
    segmented_letter = letter.readlines()

for i in range(len(list_of_invited)):
    with open(file=f"Output/ReadyToSend/letter_for_{list_of_invited[i]}.txt", mode="a") as invitation:
        first = segmented_letter[0].replace("[name]", list_of_invited[i])
        invitation.write(first)
        for j in range(1, len(segmented_letter)):
            invitation.write(segmented_letter[j])


