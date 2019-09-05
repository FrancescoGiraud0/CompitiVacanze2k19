#Giraudo Francesco Es.15 Study Drill 5

print("Type the filename: ")
filename = input("> ")

txt = open(filename) # try to open the new file called file_again and creates a file obejct called txt_again

print(txt.read()) # the method read() return a string of whatever is written in the file and then print it 

txt.close() # cloese the file