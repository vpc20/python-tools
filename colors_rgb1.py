import random


def hex_to_rgb(hex_code):
    """Converts a hex color code (e.g., '#RRGGBB' or 'RRGGBB') to an RGB tuple."""
    # Remove the '#' if present
    hex_code = hex_code.lstrip('#')
    # Convert hex to integer and extract R, G, B components
    return tuple(int(hex_code[i:i + 2], 16) for i in (0, 2, 4))


def print_colored_text(text, fg_hex, bg_hex):
    """Prints text with specified foreground and background hex colors."""
    fg_r, fg_g, fg_b = hex_to_rgb(fg_hex)
    bg_r, bg_g, bg_b = hex_to_rgb(bg_hex)

    # ANSI escape sequences for 24-bit color
    FG = f"\033[38;2;{fg_r};{fg_g};{fg_b}m"
    BG = f"\033[48;2;{bg_r};{bg_g};{bg_b}m"
    RESET = "\033[0m"

    print(f"{FG}{BG}{text}{RESET}", end='')


# Example usage:
# color_maroon = "660000"
# color_green = "006600"
# color_navy = "000066"
# color_olive = "666600"
# color_mosque = "006666"
# color_purple = "660066"

# colors = ["#00132d","#00193b","#001e45","#002657","#002d67","#00377e"]
# colors = ["#ede0d4","#e6ccb2","#ddb892","#b08968","#9c6644","#7f5539"]
# colors = ["#5c2f18","#2a4891","#008040","#ff4444","#471f71","#847244"]
# colors = ["#c1aaaa","#5555FF","#008040","#ff5555","#479999","#847244"]
# colors = ['#D66BA0', '#847244', '#198888', '#ff5555', '#5555FF', '#706fac']

for j in range(10):
    colors = [0] * 6
    for i in range(6):
        colors[i] = f"{random.randint(0, 0xd4d4d4) :06x}"
        print_colored_text(f' {colors[i]} ', "ffffff", colors[i] )
        print('   ', end='')
    print()

