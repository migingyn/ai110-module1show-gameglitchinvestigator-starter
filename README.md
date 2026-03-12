# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
   The game's purpose is to challenge the player into guessing the hidden number, providing hints to make it easier for the player.

- [X] Detail which bugs you found.
   Some bugs that I found were:
     - Inverted hint logic
        * If the guess was higher than the secret it would return a hint to go "Go Higher!" instead of lower
     - Type-mixing on even attempts
        * Secret was cast to a string for every even attempt, lexicongraphical comparison
     - Score fluctuation
        * The score would add 5 points on even attempts for wrong guesses instead of removing points
     - Offset attempts counter
        * UI displayed one fewer attempt than what was actually remaining
     - Incomplete new game button
        * Clicking New Game only reset the attempts and secret but leaves the prior game's score, status, and history
     - Mismatch debug info
        * Developer Debug info panel had an internal counter that starts ahead of the amount of guesses

- [X] Explain what fixes you applied.
   Fixes that I applied to those bugs were:
     - Inverted hint logic
        * Swapped the comparison to guess < secret
     - Type-mixing on even attempts
        * Passed secret as an int
     - Score fluctuation
        * Fixed subtraction of 5 for every incorrect guess
     - Offset attempts counter
        * Added + 1 to attempt formula to display correctly
     - Incomplete new game button
        * Reset all session state fields and sticking to the difficulty-based range
     - Mismatch debug info
        * Displayed attempts - 1 to match attempts everywhere else

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
