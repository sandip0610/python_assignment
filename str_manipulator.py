# String Manipulator
# taking sentence input
s = input("Enter a sentence: ")
print("Original:", s)

# characters count
print("Characters (with spaces):", len(s))
print("Characters (without spaces):", len(s.replace(" ", "")))
# words count
words = s.split()
print("Words:", len(words))

# case conversions
print("UPPERCASE:", s.upper())
print("lowercase:", s.lower())
print("Title Case:", s.title())

# first and last word
print("First word:", words[0])
print("Last word:", words[-1])

# reversed sentence
print("Reversed:", s[::-1])