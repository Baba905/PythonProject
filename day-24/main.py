with open("h:/Desktop/score.txt") as file:
    content = file.read()
    print(content)

with open("h:/Desktop/score.txt", mode="a") as file:
    file.write("\nNever change this mind")