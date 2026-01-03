import curses


def main(stdscr):
    # Disable automatic translation of escape sequences into KEY_UP, etc.
    stdscr.keypad(False)
    # Don't echo keys automatically; we will format them manually
    curses.noecho()

    stdscr.addstr("Press keys to see escape codes in caret notation (Press 'q' to quit):\n")

    while True:
        # getch() returns an integer representing the byte
        char_code = stdscr.getch()

        if char_code == ord('q'):
            break

        # Convert the code to caret notation if it's a control character
        # if char_code == 27:  # ESC character
        #     display = "^["
        # elif char_code < 32:
        #     display = f"^{chr(char_code + 64)}"
        # else:
        #     display = chr(char_code)
        display = chr(char_code)

        stdscr.addstr(display)
        stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
