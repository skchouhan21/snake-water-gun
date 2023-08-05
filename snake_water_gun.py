import random

def gamewin(comp, you):
    if comp == you:
        return None
    
    # Check for all possibilities when computer chose S
    elif comp == 'S':
        if you == 'W':
            return False
        elif you == 'G':
            return True
  
   # Check for all possibilities when computer chose W
    elif comp == 'W':
        if you == 'G':
            return False
        elif you == 'S':
            return True
    
     # Check for all possibilities when computer chose G
    elif comp == 'G':
        if you == 'S':
            return False
        elif you == 'W':
            return True

print("Computer Turn: Snake(S)  Water(W) or Gun(G) ")
randno = random.randint(1, 3)

if randno == 1:
    comp = 'S'
elif randno == 2:
    comp = 'W'
elif randno == 3:
    comp = 'G'

you = input("Your Turn: Snake(S) Water(W) or Gun(G): ")
a = gamewin(comp,you)

print(f"computer choose: {comp}")
print(f"You choose:  {you}")


if a == None:
    print("The game is a Tie!")
elif a:
    print("You win!")
else:
    print("You loose!")