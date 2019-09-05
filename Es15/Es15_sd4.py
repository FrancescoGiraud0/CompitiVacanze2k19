#Giraudo Francesco Es.15 Study Drill 4

from sys import argv

script, filename = argv # assign script and filename from arguments (unpack the arguments)

txt = open(filename) # open the file filename and creates a file obejct called txt

print(f"Here's your file {filename}")   # print the name of the file
print(txt.read())   # the method read() return a string of whatever is written in the file and then print it 

txt.close() # close the file