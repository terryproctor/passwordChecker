import re

strongPassword = "3YeaLink2"
mediumPassword = "yealink1"
weakPassword = "passwords"

charRegex = re.compile(r'\w{8,}')
upperRegex = re.compile(r'[A-Z]')
lowerRegex = re.compile(r'[a-z]')
digitRegex = re.compile(r'\d')

def isPasswordStrongCheck (password):
    if charRegex.search(password) and\
        upperRegex.search(password) and\
            lowerRegex.search(password) and \
                digitRegex.search(password):
                    return True
    else:
        return False

print(isPasswordStrongCheck(mediumPassword))
        
