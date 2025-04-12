"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Vladimir Dedek
email: vladimir.dedek.mx@gmail.com
"""
import random
import time

def print_intro():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

def generate_secret_number():
    digits = list("0123456789")
    first_digit = random.choice(digits[1:])  # první číslice nesmí být 0
    remaining_digits = [d for d in digits if d != first_digit]
    rest_digits = random.sample(remaining_digits, 3)
    return first_digit + ''.join(rest_digits)

def is_valid_guess(guess):
    if not guess.isdigit():
        print("Only numeric input is allowed.")
        return False
    if len(guess) != 4:
        print("Your guess must be exactly 4 digits.")
        return False
    if guess[0] == '0':
        print("Number cannot start with 0.")
        return False
    if len(set(guess)) != 4:
        print("Digits must be unique.")
        return False
    return True

def count_bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    secret_remaining = [s for s, g in zip(secret, guess) if s != g]
    guess_remaining = [g for s, g in zip(secret, guess) if s != g]

    cows = 0
    for g in guess_remaining:
        if g in secret_remaining:
            cows += 1
            secret_remaining.remove(g)
    return bulls, cows

def pluralize(word, count):
    return word if count == 1 else word + 's'

def play_game():
    secret = generate_secret_number()
    attempts = 0
    start_time = time.time()

    while True:
        print("-----------------------------------------------")
        guess = input("Enter a number:\n>>> ").strip()
        if not is_valid_guess(guess):
            continue

        attempts += 1
        bulls, cows = count_bulls_and_cows(secret, guess)
        print(f"{bulls} {pluralize('bull', bulls)}, {cows} 
              {pluralize('cow', cows)}")

        if guess == secret:
            elapsed = round(time.time() - start_time)
            print("-----------------------------------------------")
            print("Correct, you've guessed the right number")
            print(f"in {attempts} {'guess' if attempts == 1 else 'guesses'}!")
            print(f"It took you {elapsed} seconds.")
            print("-----------------------------------------------")
            print("That's amazing!")
            break

if __name__ == "__main__":
    print_intro()
    play_game()