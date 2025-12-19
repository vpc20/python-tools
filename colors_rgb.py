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
color_maroon = "660000"
color_green = "006600"
color_navy = "000066"
color_olive = "666600"
color_mosque = "006666"
color_purple = "660066"

print()
print_colored_text("", color_maroon, "1e1f22")
print_colored_text("Hello, World!", "FFFFFF", color_maroon)
print_colored_text("", color_maroon, color_green)
print_colored_text(" Python Colors", "FFFFFF", color_green)
print_colored_text("", color_green, color_navy)
print_colored_text(" Basic Colors", "FFFFFF", color_navy)
print_colored_text("", color_navy, color_olive)
print_colored_text(" Color Picker", "FFFFFF", color_olive)
print_colored_text("", color_olive, color_mosque)
print_colored_text(" RGB Colors", "FFFFFF", color_mosque)
print_colored_text("", color_mosque, color_purple)
print_colored_text(" Color Harmony", "FFFFFF", color_purple)
print_colored_text("", color_purple, "#1e1f22")
print()

# 3371FF

