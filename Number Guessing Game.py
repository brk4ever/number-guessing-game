import random

def main():
    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print(f"Try to guess the number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < target_number:
            print("Too low! Try a higher number.")
        elif guess > target_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break

    if attempts == max_attempts and guess != target_number:
        print(f"Game over! The number was {target_number}.")

if __name__ == "__main__":
    main()
