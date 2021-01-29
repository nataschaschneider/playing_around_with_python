# City country river winner - Helps you win every game!

import pandas as pd

# program data
category_answers = "C:/Users/nschn/Documents/python_code/city_country_river_winner_data_20210129.csv"
answer_df = pd.read_csv(category_answers)


# game requirements and input check
categories = input("Please enter the required categories (from city, country, river, animal, name),\n"
                   "separated by a comma, and confirm by pressing ENTER:\n")
program_categories = ["City", "Country", "River", "Animal", "Name"]
categories = categories.replace(" ", "")
categories = categories.title()
category_list = categories.split(",", 4)
while not all(x in program_categories for x in category_list):
    categories = input("That's not right. Please enter the required categories (from city, country, river, animal, name),\n"
                       "separated by a comma, and confirm by pressing ENTER:\n")
    categories = categories.replace(" ", "")
    categories = categories.title()
    category_list = categories.split(",", 4)
    continue
else:
    pass

# playing the game
def play():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "g", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letter = input("Please enter the required letter and confirm by pressing ENTER:\n")
    while not letter.lower() in alphabet:
        letter = input("That's not right. Please enter the required letter and confirm by pressing ENTER:\n")
        continue
    else:
        pass
    row_number = alphabet.index(letter.lower())

    # retrieving answers
    winning_answers = answer_df.loc[row_number, category_list]
    print(winning_answers)


game = input("\nReady to play (y/n)? Please confirm by pressing ENTER.\n")
while game.lower() != "n":
    if game.lower() != "y":
        game = input("I did not understand your input. Ready to play again (y/n)? Please confirm by pressing ENTER.\n")
        continue
    elif game.lower() == "y":
        play()
        game = input("\nReady to play again (y/n)? Please confirm by pressing ENTER.\n")
        continue
else:
    pass
input("Thank you for playing! Press ENTER to close.")
