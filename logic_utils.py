def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        # FIX: Decimal inputs like "3.7" now truncate to int instead of being left as float.
        # Claude Agent mode identified that float values broke downstream int comparisons.
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome values: "Win", "Too High", "Too Low"
    - "Too Low"  means the guess was below the secret  -> player should go higher
    - "Too High" means the guess was above the secret  -> player should go lower
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        # FIX: Swapped comparison where original had guess > secret returning "Too High"/"Go HIGHER!"
        # which was backwards. Claude Agent mode identified the inverted logic and corrected it.
        if guess < secret:
            return "Too Low", "📈 Go HIGHER!"
        else:
            return "Too High", "📉 Go LOWER!"
    except TypeError:
        # FIX: Original used str(guess) for comparison which broke int/str equality checks.
        # Claude Agent mode refactored both branches to cast to int for consistent comparison.
        g = int(guess)
        s = int(secret)
        if g == s:
            return "Win", "🎉 Correct!"
        if g < s:
            return "Too Low", "📈 Go HIGHER!"
        return "Too High", "📉 Go LOWER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    # FIX: Original had an even/odd branch that added +5 on even attempts, causing score to
    # fluctuate up and down. Claude Agent mode simplified this to always subtract 5 for wrong guesses.
    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
