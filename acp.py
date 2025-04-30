import random

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# The judge randomly chooses one number from the list
chosen_number = random.choice(number_list)

# Print the list for the contestant to see
print("Number list:", number_list)

# Ask the boy to guess the number
guess = int(input("Guess the number the judge has chosen: "))

# Check the guess
if guess == chosen_number:
    print("Congratulations! You guessed the correct number.")
elif guess < chosen_number:
    print("Your guess is too low. Try a higher number.")
else:
    print("Your guess is too high. Try a lower number.")
