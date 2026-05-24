# Password Strength Analyzer

A Python CLI tool that generates secure random passwords and evaluates password strength based on length, character diversity, and symbol distribution.

## Demo
$ python password_analyzer.py
Enter desired password length: 16
Generated Password: Xk$9mR@2wLpN!7qZ
Strength Analysis:
Length:       16 chars   ✓ Strong
Uppercase:    Yes        ✓
Lowercase:    Yes        ✓
Numbers:      Yes        ✓
Symbols:      Yes        ✓
Overall:      STRONG

## Features

- Generates passwords of any length using letters, digits, and symbols
- Evaluates strength across 5 criteria
- Gives clear pass/fail feedback per criterion
- Runs entirely from the terminal — no dependencies needed

## How to run

```bash
git clone https://github.com/kneehakiran/password-strength-analyzer
cd password-strength-analyzer
python password_analyzer.py
```

## Built with

- Python 3
- `random` and `string` modules — character pool generation

## Planned improvements

- [ ] Check password against common weak password list
- [ ] Generate passphrases (word-based passwords)
- [ ] Entropy score calculation
- [ ] Export generated passwords to a text file
