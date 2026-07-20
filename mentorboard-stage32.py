# === Stage 32: Add pagination helpers for long console output ===
# Project: MentorBoard
def paginate(lines, chunk_size=40):
    """Yield text chunks of up to `chunk_size` lines from a list of strings."""
    import sys
    for i in range(0, len(lines), chunk_size):
        chunk = '\n'.join(lines[i:i + chunk_size])
        print(chunk)

def clear_screen():
    """Clear the console screen and return to home position."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def colored(text, color):
    """Return ANSI-colored text for terminal output."""
    colors = {
        'red': '\033[91m', 'green': '\033[92m', 'yellow': '\033[93m',
        'blue': '\033[94m', 'cyan': '\033[96m', 'white': '\033[97m'
    }
    reset = '\033[0m'
    return f'{colors.get(color, "")}{text}{reset}'

def print_header(title):
    """Print a centered section header."""
    sep = '=' * 60
    print(f'\n{sep}')
    print(colored(f' {title}', 'cyan').center(60))
    print(sep)
