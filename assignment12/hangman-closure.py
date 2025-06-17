def make_hangman(secret_word: str):
    guesses = set()

    def hangman_closure(letter: str):
        nonlocal guesses
        letter = letter.lower()
        guesses.add(letter)

        display = "".join(ch if ch.lower() in guesses else "_" for ch in secret_word)
        print(display)

        return "_" not in display  # True when word is fully guessed

    return hangman_closure


if __name__ == "__main__":
    secret = input("Secret word? ").strip()
    game = make_hangman(secret)

    while True:
        guess = input("Guess a letter: ").strip()
        if game(guess):
            print("You guessed the word — congrats!")
            break