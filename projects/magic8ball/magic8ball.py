"""
Magic 8-Ball Simulator
---------------------
This script simulates a Magic 8-Ball, a toy used for fortune-telling.
It generates a random answer to a user's question based on a number from 1 to 9.
Author: Daniel Veloso
Date: August 2025
"""
import random

#define the user´s name and question
name = "Daniel"
question = "Will I land a Data Analyst job in 2025?"
answer = "" #variable to store the random answer

#Generation of random number between 1 and 9
random_number = random.randint(1,9)
#print(random_number)

#use if/else to assign answers based on the randomizer
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error" # Fallback in case of unexpected bug

# Check if the question is empty and print appropriate response
if question.strip() == "":
  print("Error, question not found.")
elif name == "": #If no name is provided
  print("Question:", question)
  print("Magic 8-Ball's answer:", answer)
# If both name and question are provided
else:
  print(name, "asks:", question)
  print("Magic 8-Ball's answer:", answer)
