# Sydney Trains Carriage Game Scripts
Python 3 scripts for the Sydney Trains carriage game

- `check.py` checks if the given number (as a command-line argument) has a solution.
- `generate.py` generates a number between 1000 and 9999 inclusive that has a solution.

## Assumptions
- There are only four valid operations: `+, -, *, /`
- `/` does not round up/down.
- The digits can be rearranged.
- `generate.py` only generates between 1000 and 9999, so there are 9000 possible numbers. With rearrangement, there are 9 * 9 * 8 * 7 = 4536 possible numbers.
