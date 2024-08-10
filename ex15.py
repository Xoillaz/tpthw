from sys import argv

script, filename = argv

# For decoding issue in Windows, I rewrite this line.
txt = open(filename, encoding='gb18030', errors='ignore')

print()

print(f"Here's your file {filename}: ")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

# Rewrite also.
txt_again = open(file_again, encoding='gb18030', errors='ignore')

print(txt_again.read())

print()

# Additional Practice
# - - -
# Comments. 
# Read manuals.
# Is there a more simple way? 
# You should close the I/O variable after calling it.
