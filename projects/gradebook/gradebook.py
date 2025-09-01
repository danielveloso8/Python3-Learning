# Gradebook Manager
# This script manages and combines student grade data using lists.
# Author: Daniel Veloso
# Date: September 1, 2025

# Initial gradebook from last semester
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Create new lists for current semester subjects and grades
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]

# Combine subjects and grades into a new gradebook
gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]

# Add new courses to the gradebook
gradebook.append(['computer science', 100])  # Add computer science with grade 100
gradebook.append(['visual arts', 93])       # Add visual arts with grade 93

# Update the visual arts grade by adding 5 points
gradebook[5][1] += 5  # Index 5 is visual arts, update the second element (grade)

# Change poetry grade from numeric to 'Pass'
gradebook[2].remove(85)  # Remove the numeric grade 85
gradebook[2].append('Pass')  # Add 'Pass' as the new grade

# Combine last semester and current semester gradebooks
full_gradebook = last_semester_gradebook + gradebook
print("Full Gradebook:", full_gradebook)  # Display the combined list of grades