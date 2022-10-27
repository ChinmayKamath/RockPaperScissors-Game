    
import random
print("WELCOME :)"

while True:
	print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
	
	# take the input from user
	choice = int(input("User turn: "))

	'''
	if any one of the condition is true
	# then it return True value
	'''
	
	# looping until user enter invalid input
	while choice > 3 or choice < 1:
		choice = int(input("enter valid input: "))
		

	# initialize value of choice_name variable
	if choice == 1:
		choice_name = 'Rock'
	elif choice == 2:
		choice_name = 'paper'
	else:
		choice_name = 'scissor'
		
	print("user choice is: " + choice_name)
	print("\nNow its computer turn.......")

	comp_choice = random.randint(1, 3)

	while comp_choice == choice:
		comp_choice = random.randint(1, 3)

	# initialize value of comp_choice_name
	# variable corresponding to the choice value
	if comp_choice == 1:
		comp_choice_name = 'Rock'
	elif comp_choice == 2:
		comp_choice_name = 'paper'
	else:
		comp_choice_name = 'scissor'
		
	print("Computer choice is: " + comp_choice_name)

	print(choice_name + " V/s " + comp_choice_name)

	# condition for winning
	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )):
		print("paper wins => ", end = "")
		result = "paper"
		
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)):
		print("Rock wins =>", end = "")
		result = "Rock"
	else:
		print("scissor wins =>", end = "")
		result = "scissor"

	# Printing either user or computer wins
	if result == choice_name:
		print("<== User wins ==>")
	else:
		print("<== Computer wins ==>")
		
	print("Do you want to play again? (Y/N)")
	ans = input()


	# if user input n or N then condition is True
	if ans == 'n' or ans == 'N':
		break
	

print("\nEND OF GAME :)")
