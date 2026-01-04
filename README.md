# secret-number-guess

---

## 🎮 Game Overview

The program generates a random integer between **1 and 10** and challenges the user to guess it. It provides feedback on whether the guess is too high or too low and continues until the user identifies the correct number. After a successful guess, the user has the option to restart the game.

### Key Logic Flow

1. **Initialization**: The `random` module is imported to generate the secret number.
2. **The Guessing Loop**:
* The user inputs a number.
* The program compares the input to the `secret_number`.
* If the guess is incorrect, it prints a hint (Higher/Lower) with emojis.
* If correct, it congratulates the user.


3. **Replay Mechanism**: A `while True` loop at the end asks the user if they want to play again.
* `tak` (yes): Resets variables and starts a new round.
* `ni` (no): Exits the program with a goodbye message.

---

## 🛠️ Technical Breakdown

| Component | Description |
| --- | --- |
| **`random.randint(1, 10)`** | Generates the target number within the specified range. |
| **`while guess != secret_number`** | Ensures the game continues until the user wins. |
| **`int(input(...))`** | Converts the user's text input into an integer for comparison. |
| **`if/elif/else`** | Logic used to provide directional feedback (too high/too low). |
| **`.lower()`** | Standardizes the replay input so "TAK" or "Tak" both work as "tak". |

---

## 💡 Code Observations

* **Humor/Style**: The code uses exaggerated strings (e.g., `"doooooooooooooo 10"`) and emojis, making it feel like a casual project or a joke among friends.
* **Redundancy**: The guessing logic is written twice (once for the first game and once inside the "play again" loop). In a professional setting, this logic would usually be wrapped in a single function to avoid repetition.
* **Error Handling**: Currently, if a user types a letter instead of a number during the guess, the program will crash with a `ValueError`.
