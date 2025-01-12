#For this project we had to complete the following:
#1. Create a greeting for the program
#2. Ask the user to pick a city; save it as a variable
#3. Ask the user to pick a pet name; save it as a variable
#4. Combine the city and pet name to display the band name

#this project is simple and straight forward and should demonstrate the understanding and use of:
# - creating and using variables
# - concatination
# - print statements
# - string manipulation
# - commenting

# says hello to the user and prompts them to enter their name.
name = input("Hello! What is your name?\n")

# welcomes the user to the program by name.
print("Welcome to the Band Name Generator!" + name)

#prompts the user to enter a city
city = input("What city did you grow up in?\n")

# prompts the user to enter the name of a pet
pet = input("What is the name of your pet?\n")

# combines the name of the city and pet to return a "band name" and says thank you to the user.
print("Your Band Name could be: " + city + " " + pet)
print("Keep on Rockin' and Thank you for trying out my program!")