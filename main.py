import random

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
---'   ____)____
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


generated_item =random.randint(0, 2)
item = [ rock, paper, scissors]

user= int(input("Enter 1) Rock 2) Paper 3) Scissors :  "))
user_item = item[user]
cpu_item = item[generated_item]


print(" User : ")
print(item[user])
print(" Cpu :")
print(item[generated_item])

if user == generated_item:
  print("try again")
elif user ==0 and generated_item == 2:
  print(" User wins")
elif user ==1 and generated_item == 0:
  print(" User wins")
elif user== 2 and generated_item == 1:
  print("user wins")
else :print(" User LOOOOOst")



