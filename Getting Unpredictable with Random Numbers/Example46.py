import random

name_list = []
name = ""

while name != "done":
    name = input('Please enter a name or "done" if you have entered all names: ')

    if name != "done":
        name_list.append(name)

print("List contains: ")
print(name_list)

random_name = random.choice(name_list)
print(f"I picked {random_name}")