friends = input("""Hello! Do you want to be friends? Y/N:
>""")
if str.lower(friends) == "y":
    name=input("""Please enter your name:
    >""")
    name=str.capitalize(name)
    print(f"""Hello, {name}! It's a pleasure to meet you!""")
    if str.lower(name) == "stefan":
        for i in range (1,10):
            print("Hallo!")
    print("You're my best friend in the world!")
else:
    print("That's okay. I've got enough friends already.")
