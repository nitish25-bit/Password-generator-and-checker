# Random Password Generator & Strength Checker

A simple command-line tool built in Python that can either **generate** a secure random password of a chosen length, or **check the strength** of a password you already have.

This was built as a beginner project to practice core Python concepts: conditionals, loops, string manipulation, and user input handling.

## Features

- **Generate mode:** Creates a random password using a mix of letters (upper and lowercase), digits, and symbols, based on a length you choose.
- **Check mode:** Scores any password you enter and rates it as **Weak**, **Medium**, or **Strong** based on its length and character variety.

## How It Works

### Generate Mode
- Enforces a minimum password length of 8 characters.
- Randomly selects characters from letters, digits, and punctuation until the password reaches your chosen length.

### Check Mode
Scoring is based on two factors:

**1. Length bonus (highest tier only counts):**
| Length | Points |
|---|---|
| 15+ characters | +4 |
| 12-14 characters | +3 |
| 10-11 characters | +2 |
| 8-9 characters | +1 |

**2. Character variety bonus (each category counts once):**
| Contains... | Points |
|---|---|
| Lowercase letter | +1 |
| Uppercase letter | +1 |
| Digit | +2 |
| Symbol | +2 |

**Final rating:**
| Total Score | Rating |
|---|---|
| 8+ | Strong |
| 5-7 | Medium |
| Below 5 | Weak |

## How to Run

Make sure you have Python 3 installed, then run:

```bash
python3 "random password generator.py"
```

Follow the on-screen prompts to either generate a password or check one.

## Example

```
Welcome to the Random Password Generator and password strength checker! Press Enter to continue...
Do you want to generate a password? or check your password strength (generate/check): generate
Enter the desired password length: 12
?ShH9wBEdV~f
password generated successfully!
```

```
Do you want to check your password strength? (yes/no): yes
Enter the password you want to check: Password123!@#
Password strength: Strong
Password strength score:  9
```

## Notes / Known Behavior

- Check mode does not enforce a minimum length before scoring — even a very short password will be scored and rated, just likely as "Weak."
- This was a learning project focused on practicing conditionals, loops, and string methods (`isupper()`, `islower()`, `isdigit()`, `any()`).

## Possible Future Improvements

- Let the user exclude ambiguous characters (like `l`, `1`, `O`, `0`) from generated passwords.
- Add an option to generate letters-only or digits-only passwords.
- Turn the repeated logic into functions for cleaner, reusable code.

## Built With

- Python 3
- Built-in `random` and `string` modules
