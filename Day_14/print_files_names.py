import glob, os

# glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell
# os module provides a portable way of using operating system dependent functionality.

os.chdir("test_dir")

print("TXT files")

for file in glob.glob("*.txt"):
    print(file)

print("ALL files")

for file in glob.glob("*"):
    print(file)