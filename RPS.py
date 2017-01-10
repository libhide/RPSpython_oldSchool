from random import randint


myDictionary = {
    "1": "Rock",
    "2": "Paper",
    "3": "Scissor",
    "q": "q"
}


def displayAndGet():
    print("1. Rock\n2. Paper\n3. Scissors\nq. Quit\n")
    ch = str(input("Your choice (enter the number): "))
    while(ch!="1" and ch!="2" and ch!="3" and ch!="q"):
        ch = str(input("Wrong choice, give proper input: "))
    return ch


def decideWinner(Sys, You):
    if Sys.choice == You.choice:
        return "none"
    elif Sys.choice == "Rock":
        return "You" if You.choice == "Paper" else "Sys"
    elif Sys.choice == "Paper":
        return "You" if You.choice == "Scissor" else "Sys"
    elif Sys.choice == "Scissor":
        return "You" if You.choice == "Rock" else "Sys"


class Player:
    ''' Applies for both human and computer'''
    def __init__(self, operator):
        self.operator = operator
        self.winCounter = 0
        self.choice = "playing"

    def bout(self):
        if self.operator == "computer":
            self.choice = myDictionary[str(randint(1, 3))]
        else:
            self.choice = myDictionary[displayAndGet()]

    def winCount(self):
        self.winCounter += 1


def main():
    YouP = Player(operator="human")
    SysP = Player(operator="computer")
    print("A Simple Rock-Paper-Scissor game")
    print("YOU vs COMPUTER")
    print("================================")
    while True:
        YouP.bout()
        if YouP.choice == "q" or YouP.choice == "Q":
            break
        SysP.bout()
        print("The computer chose {}".format(SysP.choice))
        Win = decideWinner(SysP, YouP)
        if Win == "Sys":
            print("You lost :(\n")
            SysP.winCount()
        elif Win == "You":
            print("You won :)\n")
            YouP.winCount()
        else:
            print("It's a draw!\n")
    print("==================================")
    print("Final Score:\n You: {}\n Computer: {}".format(YouP.winCounter, SysP.winCounter))
    exitInput = input("")
main()
