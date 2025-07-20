import random

# List of predefined words
words = ["apple", "robot", "tiger", "house", "train"]

# Select a random word
word = random.choice(words)
guessed_word = ["_"] * len(word)
guessed_letters = []
max_attempts = 6
wrong_guesses = 0

print("🎮 Welcome to Hangman!")
print("Guess the word letter by letter.")
print("You have", max_attempts, "wrong attempts allowed.")
print("Word:", " ".join(guessed_word))

while wrong_guesses < max_attempts and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("❗ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
        for idx, letter in enumerate(word):
            if letter == guess:
                guessed_word[idx] = guess
    else:
        wrong_guesses += 1
        print("❌ Wrong guess! Attempts left:", max_attempts - wrong_guesses)

    print("Word:", " ".join(guessed_word))
    print("Guessed letters so far:", " ".join(guessed_letters))

# Game over conditions
if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)
