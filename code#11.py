#Prog para verificar Palindromo
def palindrome(string):
    revString = string[::-1]
    if string == revString:
        print("A String é uma palindromo")
    else:
        print("A String não é um palindromo")

if __name__ == '__main__':
    
    userInput = str(input("Coloque a String que deseja verificar se é um Palindromo: "))
    palindrome(userInput)