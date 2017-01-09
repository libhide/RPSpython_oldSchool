from random import randint

myDictionary={"1":"Rock","2":"Paper","3":"Scissor","q":"q"}

def displayAndGet():
    print("1.Rock\t2.Paper\t3.Scissor")
    choice=str(input("Your Choice(Enter the number):"))
    return choice

def decideWinner(Sys,You):
    if(Sys.choice==You.choice):
        return "none"
    elif(Sys.choice=="Rock"):
        return "You" if You.choice=="Paper" else "Sys"
    elif(Sys.choice=="Paper"):
        return "You" if You.choice=="Scissor" else "Sys"
    elif(Sys.choice=="Scissor"):
        return "You" if You.choice=="Rock" else "Sys"
    
class player:
    ''' Applies for both human and computer'''
    def __init__(self,operator):
        self.operator=operator
        self.winCounter=0
        self.choice="playing"
    def bout(self):
        if(self.operator=="computer"):
            self.choice=myDictionary[str(randint(1,3))]
        else:
            self.choice=myDictionary[displayAndGet()]
    def winCount(self):
        self.winCounter+=1

def main():
    YouP=player(operator="human")
    SysP=player(operator="computer")
    print("A Simple Rock-Paper-Scissor game\nYOU vs COMPUTER\n(Type q to quit)")
    while(True):
        YouP.bout()
        if(YouP.choice=="q"):
            break
        SysP.bout()
        print("The computer chose "+SysP.choice)
        Win=decideWinner(SysP,YouP)
        if(Win=="Sys"):
            print("You lost :(\n")
            SysP.winCount()
        elif(Win=="You"):
            print("You won :)\n")
            YouP.winCount()
        else:
            print("It's a draw!\n")
    print("==================================")
    print("Final Score:\nYou:"+str(YouP.winCounter)+"\nComputer:"+str(SysP.winCounter))
    exitInput=input("")
main()
