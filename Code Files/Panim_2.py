import sys
import time

def type_text(text, delay=0.05):
    """
    Prints text one character at a time to simulate typing.
    
    Args:
        text (str): The string to print.
        delay (float): The time in seconds to wait between characters.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Forces the character to display immediately
        time.sleep(delay)
    print()  # Adds a final newline character when done

# Example usage:
message = "Hello, world! This is the typewriter effect."
type_text(message)

# Credits to Google Gemini
