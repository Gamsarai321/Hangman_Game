import random
# import string
from words import wordlist

def choice():
    return random.choice(wordlist)

# print(choice())
def printlives(l):
    print(f"you now have {l} lives left!!!!!!")



if __name__ == '__main__':
    # print(choice())
    chosenword = choice()
    print(chosenword)
    lives = len(chosenword)
    print(f"The chosen Word is {lives} letters long, so you will have only {lives} turns only.....Good Luck!!!!!!\n\n")
    userword = "-"*lives
    print("the initial word is : ",userword)
    usedletters = []
    while userword != chosenword and lives > 0:
        userinput = input("Please input a letter : ")
        # if len(userinput) > 1:
        #     print("Please input correctly")
        #     lives -= 1
        #     printlives(lives)
        #     continue
        if userinput in usedletters or userinput not in chosenword:
            print("This letter is not in word or has been already used.Please choose another......")
            lives -= 1
            printlives(lives)
        else:
            # userword = userword.replace("-",userinput,chosenword.count(userinput))
            # i = 0
            for i in range(0,len(chosenword)):
                if chosenword[i] == userinput:
                    userword = userword[:i] + userinput + userword[i+1:]
                    # print(userword,"jhedvbsafcjhsbvedfrj")
                else:
                    pass
            # i = 0
            if userword == chosenword:
                print("Congratulations!!!!!!!!!!!!!")
                print("You have succesfully guessed the word " + chosenword)
                break
            print(userword)
            usedletters.append(userinput)
            print("The used letters are : ",end=" ")
            print(" ".join(usedletters))
            # lives -= 1
            # printlives(lives)