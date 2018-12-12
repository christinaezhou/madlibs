#Assignment 2 Christina Zhou CSC131
# MADLIBS 
#The goal is to write a computer program which lets the user play Mad Libs
#reads a text file, prompts the user for words of certain parts of speech and then prints the story with the words the user provides 
#the program begins by prompting for input and output files. 
#prompts the user for another input file if the file is not found in the directory 
#place holders for parts of speech are denoted by angle brackets
#program should then ask the user if he/she would like to see the result.  If they answer yes, then your program should open the output file is opened for input and its contents displayed on the screen.


import os.path 
print("Welcome to the game of MadLibs")
print()
print("I will ask you to provide several words and phrases to fill in a MadLibs story.")
print()
print("the result will be written to an ouput file")

fileName = str(input("input file name"))

#tests to see if file exists, reprompts user if not found 
while(os.path.isfile(fileName) == False):  
   
   print(fileName, "does not exist. Try again.")
   fileName = str(input("input file name"))


outputFileName = str(input("output file name"))

fileIn= open(fileName, "r+")
fileOut = open(outputFileName, "w")

#reads the file, finds the angle brackets and prompts user to enter a replacement    
for line in fileIn.readlines():
   i=0
   x =0
   sentences = list(())
   sent = line

   while(i < len(line)):
      leftArrow =line.find("<", i, len(line))
      rightArrow = line.find(">", x, len(line))
      if(leftArrow > -1 ):
         i+=(leftArrow +1)
      
      if(rightArrow > -1):
         x +=(rightArrow+1)
       
      else:
         break
      
      replaceWord = line[leftArrow:rightArrow+1]

      userPrompt = line[leftArrow+1:rightArrow]

      phrase = str(input("Please Type a/an " + userPrompt + ":")) 
      
      sent = sent.replace(replaceWord, phrase)
      
   fileOut.write(sent)

print("Your mad libs story has been created.")

userAnswer = str(input("Would you like to see the resulting story? (Y/N)"))

if(userAnswer.upper() == "Y"):
   fileOut = open(outputFileName,"r+")
   for lineO in fileOut.readlines():
      print(lineO)

fileIn.close()
fileOut.close()

