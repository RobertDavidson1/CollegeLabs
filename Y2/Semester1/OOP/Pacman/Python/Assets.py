class Assets:
    # Define ANSI escape codes for True Color using RGB values
    RESET = "\033[0m"

    # Ghosts' colors (RGB)
    PINK = "\033[38;2;234;130;229m"  # Pink
    LIGHT_BLUE = "\033[38;2;70;191;238m"  # Light blue
    RED = "\033[38;2;255;62;25m"  # Red
    ORANGE = "\033[38;2;219;133;28m"  # Orange

    # Assets and Walls' colors (RGB)
    YELLOW = "\033[38;2;253;255;0m"  # Yellow
    BLUE = "\033[38;2;33;33;222m"  # Blue

    PACMAN = 'P'
    GHOST = 'G'
    WALL = '▀'
    FOOD = '•'
    EMPTY = ' '

    
