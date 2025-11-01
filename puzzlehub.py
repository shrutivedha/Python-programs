import random
from puzzles_data import puzzles
from datetime import datetime

def show_random_puzzle():
    """Selects and displays a random coding puzzle."""
    puzzle = random.choice(puzzles)
    print("\n🧩  PUZZLE OF THE DAY  🧩")
    print("=" * 40)
    print(f"Title: {puzzle['title']}")
    print(f"Difficulty: {puzzle['difficulty']}")
    print(f"Description: {puzzle['description']}")
    print(f"Hint: {puzzle['hint']}")
    print("=" * 40)

    # Log which puzzle was shown
    log_puzzle(puzzle)

def log_puzzle(puzzle):
    """Logs the shown puzzle into a file with a timestamp."""
    with open("logs.txt", "a") as file:
        file.write(f"{datetime.now()} - {puzzle['title']} ({puzzle['difficulty']})\n")

if __name__ == "__main__":
    print("🎉 Welcome to PuzzleHub — Your Daily Coding Challenge Generator!")
    print("Every run gives you a new puzzle to solve 🧠")
    show_random_puzzle()
    print("\nHappy coding! 🚀\n")
