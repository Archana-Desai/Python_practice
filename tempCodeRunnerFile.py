if(computer==you):
    print("It's a Draw!")
else:
    if((computer-you)==-1 or (computer-you)==2):
        print(print("You Loose !"))
    elif((computer-you)==1 or (computer-you)==-2):
        print("You won!")
    else:
        print("Something wrong in the input ")