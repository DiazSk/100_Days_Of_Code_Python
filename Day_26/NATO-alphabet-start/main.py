import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for(index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs. Exception Handling (KeyError)

while True:
    try:
        word = input("Enter a word: ").upper()
        phonetic_list = [nato_dict[letter] for letter in word]
    
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    
    else:
        print(phonetic_list)
        break