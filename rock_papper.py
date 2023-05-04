rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)___
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choose=int(input("What do you choose?\n 0 for Rock , 1 for Scissors  and 2 for Papper\n"))

if choose==0:
  print(rock)
elif choose==1:
  print(scissors)
elif choose==2:
  print(paper)
else:
  print("error")

print("computer")
import random
random_number=random.randint(0,2)
if random_number==0:
  print(rock)
elif random_number==1:
  print(scissors)
elif random_number==2:
  print(paper)

if choose==0 and random_number==1:
  print("You Win")
elif choose==0 and random_number==2: 
  print("You Loss")
elif choose==1 and random_number==0:
  print("You Loss")  
elif choose==1 and random_number==2:
  print("You Win")
elif choose==2 and random_number==0: 
  print("you Win")
elif choose==2 and random_number==1:
  print("You Loss")  
elif choose==random_number:
  print("Draw2")

