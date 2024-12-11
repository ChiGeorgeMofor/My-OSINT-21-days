result = "Results text"

results_file = open("results.txt", "a")
# The open() function has two arguments, the first the name of the file and the second the "opening mode"
# "r" - open a file for reading 
# "a" - open a file for appending 
# "w" - open a file for writing 
# "x" - create new file  

results_file.write(result) 

results_file.close()
