from random import randint

print('Goodluck')
playerchoice = input('rock (r), paper (p) or scissors (s)?')

computer = randint(1,3)
if computer == 1:
    compchoice = 'r'
elif computer == 2:
    compchoice = 'p'
else:
    computer = 's'

print(playerchoice)
print('VS')
print(compchoice)

if playerchoice == compchoice: 
    print('DRAW!')
elif playerchoice == 'r' and compchoice == 's':
    print('YOU WIN!')
elif playerchoice == 'r' and compchoice == 'p':
    print("YOU LOSE!")
elif playerchoice == 'p' and compchoice == 'r':
    print('YOU WIN!')
elif playerchoice == 'p' and compchoice == 's':
    print('YOU LOSE!')
elif playerchoice == 's' and compchoice == 'p':
    print('YOU WIN!')
elif playerchoice == 's' and compchoice == 'r':
    print('YOU LOSE!')


