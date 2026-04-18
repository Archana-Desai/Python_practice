import random

''' We are creating a small game of snake water gun game
Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water
Gun vs. Snake: Gun will kill the snake and win.'''

choices={"s":1,"w":0,"g":-1}
computer=random.choice(list(choices.values()))
youstr=input("Enter any one of these vales:s,w,g   ")
you=choices.get(youstr)
print(computer)

if(computer==you):
    print("It's a Draw!")
else:
    if ((computer==1 and you==-1) or (computer==-1 and you==0) or(computer==0 and you==1)):
        print("You Loose !")
    elif((computer==1 and you==0) or (computer==-1 and you==1) or(computer==0 and you==-1)):
        print("You won !")
    else:
        print("Something wrong in the input ")

