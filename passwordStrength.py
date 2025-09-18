import re
level = 0
tryAgain = True
# Ask for a password input

# Create function for checking password length
def passwordLength(password):
    length = len(password)
    global level
    if length >= 5 and length < 8:  # Check password for string length
        level += 1
    elif length >= 8 and length < 12:
        level += 2
    elif length >= 12:
        level +=3
    

# Check password for numbers
def passwordNumbers(password):
    global level
    numberRegex = re.compile(r'\d')
    extractedNumber = numberRegex.findall(password)
    if len(extractedNumber) > 0 and len(extractedNumber) < 3:
        level += 1
    if len(extractedNumber) >= 3:
        level += 2
        
# Check Password for other characters
def passwordExtras(password):
    global level
    extrasRegex = re.compile(r'[^a-zA-Z0-9]')
    extractedExtras = extrasRegex.findall(password)
    if len(extractedExtras) > 0 and len(extractedExtras) < 3:
        level += 1
    if len(extractedExtras) >= 3:
        level += 2
        
# Asks if you want to try a new password
def newPassword():
    global tryAgain
    print('Would you like to try another password?')
    answer = input('y/n: ').strip().lower()
    if answer == 'y':
        tryAgain = True
    elif answer == 'n':
        tryAgain = False
    else:
        print('Please enter y or n.')
        newPassword()
# Put everything together

def together():
    global level
    global tryAgain
    while tryAgain == True:
        level = 0
        password = input('Enter Password: ')
        print(password)
        tryAgain = True
        passwordLength(password)
        passwordNumbers(password)
        passwordExtras(password)
        if level == 0:
            print('Extremely weak password')
        elif level == 1:
            print('Very weak password')
        elif level == 2:
            print('Weak password')
        elif level == 3:
            print('Adequate password')
        elif level == 4:
            print('Good password')
        elif level == 5:
            print('Great password')
        elif level == 6:
            print('Extremely difficult password')
        elif level == 7:
            print('Unbreakable password')
            break
        
        newPassword()

together()
            
