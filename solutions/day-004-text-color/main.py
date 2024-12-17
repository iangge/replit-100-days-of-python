print("""Welcome to the adventure simulator! I'm going to ask some questions and then create an epic story with you as the star!\n""")

name = input("What is your name? ")
enemy = input("Give the name of an enemy: ")
superpower = input("What is your superpower? ")
location = input("Where do you live? ")
food = input("What is your favorite food? ")
print()

print(f"""Hello {name}! Your power of \033[36m{superpower}\033[0m""")
print(f"""will make sure you never have to look at {enemy} again. Go eat {food} as you walk down the streets of {location}""")
