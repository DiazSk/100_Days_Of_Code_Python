import os

PLACEHOLDER = "[name]"

try:
    with open("Input/Names/invited_names.txt", mode="r", encoding="utf-8") as names_file:
        names = names_file.read().splitlines()

    with open("Input/Letters/starting_letter.txt", mode="r", encoding="utf-8") as letter_file:
        letter = letter_file.read()

    # Ensure output directory exists
    os.makedirs("Output/ReadyToSend", exist_ok=True)

    for name in names:
        if name.strip():  # Skip empty lines
            cleaned_name = name.strip()
            new_letter = letter.replace(PLACEHOLDER, cleaned_name)
            
            # Sanitize filename
            safe_filename = "".join(c for c in cleaned_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
            
            with open(f"Output/ReadyToSend/letter_for_{safe_filename}.txt", mode="w", encoding="utf-8") as output_file:
                output_file.write(new_letter)

    print(f"Successfully created letters for {len([name for name in names if name.strip()])} recipients.")

except FileNotFoundError as e:
    print(f"Error: Could not find file {e.filename}")
    print("Please make sure the Input files exist.")
    
except Exception as e:
    print(f"An error occurred: {e}")