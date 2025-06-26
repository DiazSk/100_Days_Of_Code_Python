def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    
    # Count occurrences of letters in "TRUE"
    true_count = 0
    for letter in "true":
        true_count += combined_names.count(letter)
    
    # Count occurrences of letters in "LOVE"
    love_count = 0
    for letter in "love":
        love_count += combined_names.count(letter)
    
    # Combine to make a 2-digit number
    love_score = int(str(true_count) + str(love_count))
    
    return love_score

# Test cases
print(f"Zaid and Aafiya: {calculate_love_score('Zaid', 'Aafiya')}")
print(f"Romeo and Juliet: {calculate_love_score('Romeo', 'Juliet')}")
print(f"Brad Pitt and Angelina Jolie: {calculate_love_score('Brad Pitt', 'Angelina Jolie')}")
print(f"Harry Potter and Hermione Granger: {calculate_love_score('Harry Potter', 'Hermione Granger')}")
print(f"John Smith and Jane Doe: {calculate_love_score('John Smith', 'Jane Doe')}")
print(f"Kanye West and Kim Kardashian: {calculate_love_score('Kanye West', 'Kim Kardashian')}")