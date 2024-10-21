options = ["1","2"]
inventorycp = ["celery sword"]
inventorycm = ["cilly staf"]
inventorybb = ["brusersprout bombs"]
#this is how we make a function
def pickclass():
 print("you are in the kingdom of Cake")
 print("we are in a war against the dintest coalition")
 print("it's your job to fight the dintests")
 print("please pick a class")
 print("____________________")
 print("celery paladin")
 print("____________________")
 print("cilly mage")
 print("____________________")
 print("brusersprout bomber ")
 print("____________________")
 userinput = input("1,2,3")
 if userinput == "1":
    print("you are a celery paladin ")
    cp()

 elif userinput == "2":
    print("you are a cilly mage")
    cm()

 elif userinput == "3":
    print("you are a brusersprout bomber")
    bb() 
def shop():
 print()




def cp():
 print("now you go to the shop")
 shop()
 print("your frist mission is to the choclate falls to investigate a suspicious man")
 print("that seems to be cleaned up the choclate")



def cm():
 print("your frist mission is to the choclate falls to investigate a suspicious man")
 print("that seems to be cleaned up the choclate")



def bb():
 print("your frist mission is to the choclate falls to investigate a suspicious man")
 print("that seems to be cleaned up the choclate")



def intro():
    print(" Hello brave adveturer")
    name = userinput 
    name = input("please put in your name")
    if name == "":
        print("please pick your heain")
    else:
        print('welcome')
        print(f'{name}')
        print("========================================================")
        pickclass()
  




if __name__ in "__main__":
    #Introduction to game 
    print("welcome to the hunt for the pizza rolls")

    userinput = ""

 ##checks to see if the user inputs a valid option
while userinput not in options:
    userinput = input("press 1 to start press 2 to exit")

    if userinput == "1":
        intro()

    elif userinput == "2":
        print("goodbye")
    else:
        print("please enter a valid number")











