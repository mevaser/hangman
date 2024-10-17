import random
import hangman_words
import hangman_art

# Initial number of lives
lives = 6

# Print the game logo from hangman_art.py
print(hangman_art.logo)

# Choose a random word from the word list in hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
print(f"Pssst, the solution is: {chosen_word}")  # Debugging hint, can be removed for production

# Create a placeholder string with underscores based on the length of the chosen word
placeholder = "_" * len(chosen_word)
print(f"Word to guess: {placeholder}")

# Flag to indicate when the game is over
game_over = False

# List to store all guessed letters
guessed_letters = []

# Main game loop
while not game_over:
    # Display how many lives the player has left
    print(f"****************************{lives} LIVES LEFT****************************")

    # Display the letters already guessed
    print(f"Guessed letters: {guessed_letters}")

    # Get a letter guess from the user
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        continue

    # Add the guess to the guessed letters list using append
    guessed_letters.append(guess)

    # Create a new string to update the word display
    display = ""

    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display += guess  # Add the guessed letter at the correct position
            else:
                display += placeholder[index]  # Keep previously guessed letters or underscores
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1  # Reduce lives if the guess is incorrect
        display = placeholder  # If the guess is wrong, no change in the displayed word

    # Update the placeholder with the new display
    placeholder = display
    print(f"Word to guess: {placeholder}")

    # Check if the player has lost (no lives left)
    if lives == 0:
        game_over = True
        print(f"****************************IT WAS {chosen_word}! \nYOU LOSE****************************")

    # Check if the player has won (no underscores left)
    if "_" not in placeholder:
        game_over = True
        print("****************************YOU WIN****************************")
        print(f"The word was: {chosen_word}")

    # Display the current hangman stage based on the number of lives left
    print(hangman_art.stages[lives])
