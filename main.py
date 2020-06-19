import random

informationsList = []

numbersList = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

lettersList = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'x', 'z'
]

capitalLettersList = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'X', 'Z'
]

# get informations of user
def informations():

    numberDigits = 0
    letters = False
    capitalLetters = False

    # amount numbers
    j = True
    while(j):
        try:
            numberDigits = int(input("Quantos caracteres sua senha necessita?   "))
            j = False

        except:
            print("Por favor digite uma resposta válida!")


    # type of caracters
    k = True
    while(k):
        try:
            needLetters = input("Necessita de letras? (s/n)   ")

            if(needLetters == "s"):
                letters = True
                k = False
            elif(needLetters == "n"):        
                k = False


            if(letters):
                z = True
                while(z):

                    try:
                        needCapitalLetters = input("Necessita de letras maiusculas? (s/n)   ")

                        if(needCapitalLetters == "s"):
                            capitalLetters = True
                            z = False
                        elif(needCapitalLetters == "n"):
                            z = False
                        
                    except:
                        print("Por favor digite uma resposta válida!")

                    print("Por favor digite uma resposta válida!")

        except:
            print("Por favor digite uma resposta válida!")

        print("Por favor digite uma resposta válida!")
    
    informationsList.append(numberDigits)
    informationsList.append(letters)
    informationsList.append(capitalLetters)

def generatePassword(numberDigits, letters, capitalLetters):

    password = ""
    i = 0
    while( i < numberDigits):
        
        # the elements compete with each other to enter the password
        elementCompetition = []
        
        randomNumber = str(random.randint(0, 9))

        # append randons caracters to the war list
        elementCompetition.append(randomNumber)

        if(letters):

            # get a random element of letter list
            x = random.randint(0, ( (len(lettersList))-1) )
            randomLetter = lettersList[x]

            # append randons cararters to the war list
            elementCompetition.append(randomLetter)

            if(capitalLetters):
                # get a random element of capital letters list
                y = random.randint(0, ( (len(capitalLettersList))-1) )
                randomCapitalLetter = capitalLettersList[y]

                # append randons cararters to the war list
                elementCompetition.append(randomCapitalLetter)
                

        # get a random element of a war list and
        x = random.randint(0, ( (len(elementCompetition))-1) )
        randomElement = elementCompetition[x]
        
        # insert random element to the password
        password = password + randomElement

        i += 1

    return password

informations()

password = generatePassword(informationsList[0], informationsList[1], informationsList[2])

# return for the user
print("Aqui está sua senha: " + password)