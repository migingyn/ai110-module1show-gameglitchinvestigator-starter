from logic_utils import check_guess, parse_guess


# --- Bug: swapped higher/lower hints (fixed in commit 8d05c3e) ---
# Original code had `guess > secret` returning "Too High" with "Go HIGHER!" —
# the comparison operator was inverted so the outcome label was backwards.

def test_guess_below_secret_is_too_low():
    # guess=40 is below secret=50 → player should go HIGHER → outcome "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low", f"Expected 'Too Low' but got '{outcome}'"
    assert "HIGHER" in message, f"Expected hint to say go higher, got: '{message}'"

def test_guess_above_secret_is_too_high():
    # guess=60 is above secret=50 → player should go LOWER → outcome "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High", f"Expected 'Too High' but got '{outcome}'"
    assert "LOWER" in message, f"Expected hint to say go lower, got: '{message}'"

def test_exact_guess_is_win():
    # guess == secret → Win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win", f"Expected 'Win' but got '{outcome}'"


# --- Bug: secret passed as string on even attempts (fixed in commit d252ef3) ---
# Every other attempt, app.py converted the secret to a str before calling
# check_guess, causing int/str comparison to fail silently or give wrong hints.

def test_check_guess_when_secret_is_string_too_low():
    # Simulates the even-attempt bug: secret accidentally passed as str
    # check_guess must still correctly identify guess < secret
    outcome, message = check_guess(30, "50")
    assert outcome == "Too Low", f"Type-mixing bug: expected 'Too Low', got '{outcome}'"
    assert "HIGHER" in message

def test_check_guess_when_secret_is_string_too_high():
    outcome, message = check_guess(70, "50")
    assert outcome == "Too High", f"Type-mixing bug: expected 'Too High', got '{outcome}'"
    assert "LOWER" in message

def test_check_guess_when_secret_is_string_win():
    outcome, message = check_guess(50, "50")
    assert outcome == "Win", f"Type-mixing bug: expected 'Win', got '{outcome}'"


# --- Bug: parse_guess must always return int, never float (commit d252ef3) ---
# Decimal inputs like "3.7" should be truncated to int, not left as float,
# so that downstream int comparisons work correctly.

def test_parse_guess_integer_string():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert isinstance(value, int), f"Expected int, got {type(value)}"

def test_parse_guess_decimal_string_truncates_to_int():
    # "3.7" must parse to int 3, not float 3.7
    ok, value, err = parse_guess("3.7")
    assert ok is True
    assert isinstance(value, int), f"Expected int from decimal input, got {type(value)}"
    assert value == 3

def test_parse_guess_empty_string_fails():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_guess_none_fails():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None

def test_parse_guess_non_numeric_fails():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
