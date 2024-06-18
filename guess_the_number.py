import random
gen_number = random.randint(1, 100)
points = 10

while True:
	guess = int( input("guess the number:  "))

	if gen_number == guess:
		print(f"you guessed the number and you achived {points} points")
		break
	elif gen_number > guess: 
		if gen_number - guess <= 2:
			print("Too Close & Too Low")
		else:
			print("Too Low")
		points -= 1
	elif gen_number < guess:
		if guess - gen_number <= 2:
			print("Too Close & Too High")
		else:
			print("Too High")
		points -= 1

	if points < 1:
		print("You lose the game boooo...😯😯😯")
		print(f"The guessing number is {gen_number}")
		break
