import string
import random
import time

keepUsing = True
length = 0


pswNumber = list(string.digits)
pswLetter = list(string.ascii_letters)
pswSpecial = list(string.punctuation)
pswAll = pswSpecial + pswLetter + pswNumber



while keepUsing == True:
    random.shuffle(pswAll)


    #Password length by user input w/ min length of 15 chars
    while True:
        try:
            length = int(input("Enter the password length: "))
            if length < 15:
                print("Your password should be minimum 15 characters")
            else:
                break
        except:
            ValueError()
            print("Enter a number")


    #empty list of chars in password
    passwordList = []

    #appending random chars to password list
    for i in range(length):
        randomChar = random.choice(pswAll)
        passwordList.append(randomChar)

    #joining password to empty string
    password = ''.join(passwordList)

    #printing password
    print("Your safe password: ", password )
    while True:
        try:  
            anotherOne = str(input("Do You want to generate another password? Press Y to continue or N to exit: ")).lower()
            if anotherOne in ['y', 'n']:   
                if anotherOne == "y":
                    keepUsing = True
                    break
                if anotherOne == "n" :
                    keepUsing = False
                    break
            else:
                ValueError()
                print("Enter Y or N")
        except:
            ValueError()
            print("Enter Y or N")
            
print("Thank You for using my password generator. App is closing...")
time.sleep(2)


    



