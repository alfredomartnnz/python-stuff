#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3

print("hello")

#variable
message = "hello python world"
print(message)
#variable
message = "hello python crash course world!"
print(message)

#all first words are capitalized .title()
#everything upper .upper()
#everything lower .lower()
#this is called a METHOD .title() .upper()  .lower()
name = "i love to eat protein"
print(name.title())
print(name.lower())
print(name.upper())

#variable example
name = "alfredo"
print(name)

#f-string / method example
first_name = "alfredo"
last_name = "martinez"
full_name = f"{first_name} {last_name}"
print(f"goodbye, {full_name.title()}!")

#f-string / method example
first_name = "alfredo"
last_name = "martinez"
full_name = f"{first_name} {last_name}"
full_name = f"{first_name.upper()} {last_name.lower()}"
print(f"goodbye, {first_name.upper()}!")
print(full_name)

#f-string / method example
message = f"goodbye, {full_name.upper()}!"
print(message)

#whitespace
#tab
print("\tAlfredo loves pasta more than Nelli does")

#newline
print("List of chores:\nclean bathroom\nwash dishes\nmop the living room")
