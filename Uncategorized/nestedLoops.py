"""
Protram to print all wo-letter domain names.

ord('a') --> take a character and return its ASCII number
chr(97) --> take an ASCII number and return its character
"""

print("\n\nTwo-letter domain:")
count = 0
letter1 = "a"
letter2 = "?"
while letter1 <= "z":       # Outer loop
    letter2 = "a"
    while letter2 <= "z":        # Inner loop
        print(f"{letter1}{letter2}.com")
        letter2 = chr(ord(letter2) + 1)       # Protects us from infinite loop
        count += 1
    letter1 = chr(ord(letter1) + 1)       # Protects us from infinite loop


print(count)