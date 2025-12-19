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
color1 = "AA0000"
color2 = "00AA00"
color3 = "0000AA"
color4 = "AAAA00"
color5 = "00AAAA"
color6 = "AA00AA"

print()
print_colored_text("", color1, "1e1f22")
print_colored_text("Hello, World!", "FFFFFF", color1)
print_colored_text("", color1, color2)
print_colored_text(" Python Colors", "FFFFFF", color2)
print_colored_text("", color2, color3)
print_colored_text(" Next String", "FFFFFF", color3)
print_colored_text("", color3, color4)
print_colored_text(" More String", "FFFFFF", color4)
print_colored_text("", color4, color5)
print_colored_text(" RGB Colors", "FFFFFF", color5)
print_colored_text("", color5, color6)
print_colored_text(" Color Harmony", "FFFFFF", color6)
print_colored_text("", color6, "#1e1f22")
print()

# 3371FF

