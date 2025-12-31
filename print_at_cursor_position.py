import sys
import time

def print_at_position(text, row, col):
    """
    Prints text at a specific row and column in the console.
    Note: Coordinates are typically 1-based (row 1, col 1 is top-left).
    """
    print(f"\033[{row};{col}H{text}")

# Example usage

# Clears the screen and moves the cursor to the top-left
print("\033[H\033[2J", end="")

print_at_position("Hello, world!", 5, 10)
print_at_position("This text is at a specific spot.", 10, 5)
# Move cursor to a new line at the bottom to continue standard printing
print_at_position("", 15, 1) # Move to row 15, column 1
print("Done.")
