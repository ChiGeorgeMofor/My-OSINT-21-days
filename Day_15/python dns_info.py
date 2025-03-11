import python dns
import dns.resolver

result = dns.resolver.resolve('osintme.com', 'A')
for ipval in result:
    print('IP', ipval.to_text())
# Compare this snippet from Day_14/check_files_contents.py:
# import glob, os
#
# os.chdir("test_dir")
#
# for file in glob.glob("*"):       # for file in glob.glob("*"):  # for file in glob.glob("*"):  # for file in glob.glob("*txt"):
#     with open(file) as current_file:
#         current_file_content=current_file.read()
#      current_file_content=current_file.read() # current_file_content=current_file.read()  # current_file_content=current_file.read()