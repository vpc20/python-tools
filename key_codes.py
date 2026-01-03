import curses

def main(stdscr):
    curses.noecho()  # Don't print keys automatically
    stdscr.addstr("Press any key (Press 'q' to quit):\n")
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
        stdscr.addstr(f"Key Code: {key}\n")
        stdscr.refresh()

curses.wrapper(main)
