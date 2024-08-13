from sys import argv
from os.path import exists

script, from_file, to_file = argv

print()

print(f"Copying from {from_file} to {to_file}")

# We could do these two in one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

print()

# Additional Practice
# - - -
# Try streamline the script.
# Try transform the script into 1 line.
    # That; depends; on; how; you; define; one; line; of; code. 
# Read manual.
# Every line matters.
