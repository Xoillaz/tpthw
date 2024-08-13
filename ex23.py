import sys
script, encoding, error = sys.argv

def main(lang_file, encoding, errors):
    line = lang_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(lang_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<==>", cooked_string)

print()

langs = open("ex23_langs.txt", encoding = "utf-8")

main(langs, encoding, error)

print()

# Additional Practice
# - - -
# Review and explain.
# Try broke the code and repair.
