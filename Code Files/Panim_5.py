import sys
import time

def retro_cursor_type(text, delay=0.08):
    cursor = "█" 
    
    for char in text:
        # Print the character AND the cursor
        sys.stdout.write(char + cursor)
        sys.stdout.flush()
        
        time.sleep(delay)
        
        # Backspace over the cursor so the next loop overwrites it
        # (We use \b to move back one space)
        sys.stdout.write('\b')
        sys.stdout.flush()

    print() # Final newline

# Example usage:
retro_cursor_type("C:\\> ESTABLISHING CONNECTION...")

# Credits to Google Gemini
