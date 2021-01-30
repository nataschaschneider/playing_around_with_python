# City country river winner - Helps you win every game!

# libraries and modules
import pandas as pd
from tabulate import tabulate

# program data
category_answers = "C:/Users/nschn/Documents/python_code/city_country_river_winner_data_20210129.csv"
answer_df = pd.read_csv(category_answers)
alphabet = answer_df["Letter"].tolist()
answer_df.set_index("Letter", drop=True, inplace=True)

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
    letter = input("Please enter the required letter and confirm by pressing ENTER:\n")
    letter = letter.upper()
    while letter not in alphabet:
        letter = input("That's not right. Please enter the required letter and confirm by pressing ENTER:\n")
        letter = letter.upper()
        continue # you don't need a "continue" at the end of a loop. Doppelt gemoppelt as we Germans say. 
    else:
        pass
    # retrieving answers
    winning_answers = answer_df.loc[[letter], category_list]
    print(tabulate(winning_answers, headers=category_list, tablefmt='fancy_grid'))


game = input("\nReady to play (y/n)? Please confirm by pressing ENTER.\n")
while game.lower() != "n":
    if game.lower() != "y":
        game = input("I did not understand your input. Ready to play again (y/n)? Please confirm by pressing ENTER.\n")
        continue # unnecessary continue as well
    elif game.lower() == "y":
        play()
        game = input("\nReady to play again (y/n)? Please confirm by pressing ENTER.\n")
        continue # yup, you guessed it :) 
else:
    pass
input("Thank you for playing! Press ENTER to close.")
