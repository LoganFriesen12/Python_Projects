import re
import os

#Asks user for keyword to search for
keyWord = input('What keyword would you like to search for? ')
#Asks user for directory to work in
currentDirectory = input("Paste the full directory name you would like to work in: ")
print("\n")
#Sets keyword to search for and what directory to work in
regexKeyword = re.compile(keyWord, re.IGNORECASE)
os.chdir(currentDirectory)


#Iterates over filenames in directory
for fileName in os.listdir():
    if fileName.endswith('.txt'):
        with open(fileName, "r", encoding="utf-8") as file:
                  for line_number, line in enumerate(file, start=1):
                      if regexKeyword.search(line):
                          print(f"File: {fileName} \n Line {line_number}: {line}")
