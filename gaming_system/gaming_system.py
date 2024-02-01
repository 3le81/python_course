"""
Instructions for Testing the Program:

1. Run the program.
2. Ensure to enter the correct username and password. If the user doesn't exist, register before attempting to login.
3. Choose a game to play.
4. Choose option for playing, checking game history, logout or exit.
"""

import os
import pickle
import random

# Constants for game states
MENU = 0
PLAYING = 1
PAUSED = 2

# File paths
GAMING_SYSTEM_PATH = "gaming_system"
USER_DATA_PATH = os.path.join(GAMING_SYSTEM_PATH, "user_data")
SAVED_GAMES_PATH = os.path.join(GAMING_SYSTEM_PATH, "saved_games")
LEADERBOARDS_PATH = os.path.join(GAMING_SYSTEM_PATH, "leaderboards")
USER_DETAILS_PATH = os.path.join(USER_DATA_PATH, "user_details.txt")
GAME_HISTORY_PATH = os.path.join(GAMING_SYSTEM_PATH, "game_history.pickle")

# Global data
user_data = []       # User account information (username, password)
game_history = {}    # Dictionary to store user game history

# Function to clear the console screen


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Function to create necessary folders


def create_folders():
    folders = [GAMING_SYSTEM_PATH, USER_DATA_PATH,
               SAVED_GAMES_PATH, LEADERBOARDS_PATH]

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)


# Call the function to create folders
create_folders()

# Function to load user data from file


def load_user_data():
    if os.path.exists(USER_DETAILS_PATH):
        with open(USER_DETAILS_PATH, "r") as file:
            return [line.strip().split(", ") for line in file]
    return []

# Function to save user data to file


def save_user_data():
    with open(USER_DETAILS_PATH, "w") as file:
        for username, password in user_data:
            file.write(f"{username}, {password}\n")

# Function to load game history from file


def load_game_history():
    if os.path.exists(GAME_HISTORY_PATH):
        with open(GAME_HISTORY_PATH, "rb") as file:
            return pickle.load(file)
    return {}

# Function to save game history to file


def save_game_history():
    with open(GAME_HISTORY_PATH, "wb") as file:
        pickle.dump(game_history, file)

# Function for user registration


def register_user():
    global user_data
    print("\n=== User Registration ===")
    username = input("Enter your username: ")

    # Check if the username already exists
    if any(username == user[0] for user in user_data):
        print("Username already exists. Please choose another.")
        return

    # Prompt the user to enter a password
    password = input("Enter your password: ")

    # Add the user to the user_data list
    user_data.append((username, password))

    # Save the updated user data to file
    save_user_data()

    print("User registration successful!")

# Function for user login


def login_user():
    global user_data
    print("\n=== User Login ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the user exists
    user_exists = any(username == user[0] for user in user_data)

    if user_exists:
        # Find the user with the entered username
        user = next(user for user in user_data if user[0] == username)

        # Compare the entered password to the stored password
        if password == user[1]:
            print("Login successful! Welcome,", username)
            return username
        else:
            print("Incorrect password. Please try again.")
            return None
    else:
        print("User not found. Please register before attempting to login.")
        return None


# Function to display the menu

def display_menu():
    print("\n=== Game Menu ===")
    print("1. Play Guess the Number")
    print("2. Play Hangman")
    print("3. View Game History")
    print("4. Logout")
    print("5. Exit")


# Function to play the Guess the Number game
def play_guess_the_number():
    print("\n=== Guess the Number ===")
    # Implement Guess the Number game logic here
    # For example:
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (between 1 and 100): ")

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess == secret_number:
            print(
                f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            return ("Guess the Number", 100)  # Returning a tuple
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Function to play the Hangman game


def play_hangman():
    print("\n=== Hangman ===")
    word_to_guess = random.choice(["python", "program", "holidays"])
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    while attempts < max_attempts:
        # Display the current state of the word
        display_word = "".join(
            letter if letter in guessed_letters else "_" for letter in word_to_guess)
        print(f"Word: {display_word}")

        # Get user guess
        guess = input("Enter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            # Check if the guessed letter is in the word
            if guess in word_to_guess:
                print("Correct!")
                guessed_letters.add(guess)
            else:
                print("Incorrect!")
                attempts += 1
        else:
            print("Invalid input. Please enter a single letter.")

        # Check if the word is completely guessed
        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You guessed the word: {word_to_guess}")
            return ("Hangman", 100)  # Returning a tuple

    print(
        f"Sorry, you've run out of attempts. The correct word was: {word_to_guess}")
    return ("Hangman", 0)  # Returning a tuple


# Function to play a game based on user choice
def play_game():
    global game_history, current_user

    while True:
        print("\n=== Game Menu ===")
        print("1. Play Guess the Number")
        print("2. Play Hangman")
        print("3. View Game History")
        print("4. Logout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            game_result = play_guess_the_number()
            if game_result is not None:
                score = game_result
                game_history.setdefault(current_user, []).append({
                    "game_id": len(game_history.get(current_user, [])) + 1,
                    "game": "Guess the Number",
                    "score": score,
                })
                save_game_history()

        elif choice == "2":
            game_result = play_hangman()
            if game_result is not None:
                score = game_result
                game_history.setdefault(current_user, []).append({
                    "game_id": len(game_history.get(current_user, [])) + 1,
                    "game": "Hangman",
                    "score": score,
                })
                save_game_history()

        elif choice == "3":
            view_game_history()

        elif choice == "4":
            current_user = None
            clear_screen()
            print("Logged out. See you next time!")
            break

        elif choice == "5":
            print("Thank you for using PlayMaster. Goodbye!")
            exit()  # Terminate the program

        else:
            print("Invalid choice. Please try again.")


# Helper function to handle game results


def handle_game_result(game_result):
    global game_history, current_user

    if game_result is not None:
        game, score = game_result
        game_history.setdefault(current_user, []).append({
            "game_id": len(game_history.get(current_user, [])) + 1,
            "game": game,
            "score": score,
        })
        save_game_history()

# Helper function to logout the user


def logout_user():
    global current_user

    current_user = None
    clear_screen()
    print("Logged out. See you next time!")


# Function to view user's game history


def view_game_history():
    global game_history
    print("\n=== Game History ===")
    for username, games in game_history.items():
        print(f"\n{username}'s Games:")
        for game in games:
            print(
                f"   - Game ID: {game['game_id']}, Game: {game['game']}, Score: {game['score']}")

# Function to implement scoring and ranking


def calculate_score(game_type, game_duration):
    # Example: Score based on game duration
    if game_duration < 30:
        return 100
    elif game_duration < 60:
        return 75
    else:
        return 50


# Main program execution
def main():
    # Declare current_user as a global variable
    global user_data, game_history, current_user
    user_data = load_user_data()
    game_history = load_game_history()
    current_user = None

    while True:
        if current_user is None:
            print("\n=== Welcome to PlayMaster ===")
            print("Login: Users must log in before accessing the game.")
            print("If you don't have an account, you can register.")

            choice = input("Enter 'login', 'register', or 'exit': ").lower()
            if choice == "login":
                current_user = login_user()
                if current_user:
                    print(f"Welcome, {current_user}!")
            elif choice == "register":
                register_user()
            elif choice == "exit":
                print("Thank you for using PlayMaster. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                game_result = play_guess_the_number()
                if game_result is not None:
                    game, score = game_result
                    game_history.setdefault(current_user, []).append({
                        "game_id": len(game_history.get(current_user, [])) + 1,
                        "game": game,
                        "score": score,
                    })
                    save_game_history()
            elif choice == "2":
                game_result = play_hangman()
                if game_result is not None:
                    game, score = game_result
                    game_history.setdefault(current_user, []).append({
                        "game_id": len(game_history.get(current_user, [])) + 1,
                        "game": game,
                        "score": score,
                    })
                    save_game_history()
            elif choice == "3":
                view_game_history()
            elif choice == "4":
                logout_user()
            elif choice == "5":
                print("Thank you for using PlayMaster. Goodbye!")
                exit()  # Terminate the program
            else:
                print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()
