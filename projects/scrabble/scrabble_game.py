# Scrabble Score Calculator
# This script calculates points for words based on letter values and tracks player scores.
# Author: Daniel Veloso
# Date: September 4, 2025

# Initial list of uppercase letters for Scrabble
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Corresponding points for each letter based on Scrabble rules
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Add lowercase letters to the list for case-insensitive scoring
letters += [letter.lower() for letter in letters]

# Duplicate points list to match the doubled letters (uppercase and lowercase)
points *= 2

# Create a dictionary mapping letters to their points using zip
letter_to_points = {key: value for key, value in zip(letters, points)}
# print(letter_to_points)  # Uncomment for debugging

# Add a point value for blank spaces (0 points)
letter_to_points[" "] = 0

# Calculate the score of a given word
def score_word(word):
    """Calculate the total score of a word based on letter points."""
    point_total = 0
    for letter in word.upper():  # Convert to uppercase for consistency
        point_total += letter_to_points.get(letter, 0)  # Default to 0 for unknown letters
    return point_total

# Test the score_word function with "BROWNIE"
brownie_points = score_word("BROWNIE")
print(f"Score for 'BROWNIE': {brownie_points}")  # Expected: 15 (B:3, R:1, O:1, W:4, N:1, I:1, E:1)

# Dictionary mapping players to their list of words
players_to_words = {
    'player1': ['BLUE', 'TENNIS', 'EXIT'],
    'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
    'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],  # Corrected 'HUESKY' to 'HUSKY' (typo)
    'Prof Reader': ['ZAP', 'COMA', 'PERIOD']
}

# Dictionary to store total points per player
player_to_points = {}

# Update total points for each player based on their words
def update_point_totals():
    """Update the total points for each player based on their word scores."""
    for player, words in players_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

# Execute the points update
update_point_totals()
print(f"Player Points: {player_to_points}")  # Expected: {'player1': 14, 'wordNerd': 22, ...}

# Function to add a new word to a player's list
def play_word(player, word):
    """Add a new word to the specified player's word list."""
    if player in players_to_words:  # Check if player exists
        players_to_words[player].append(word.upper())  # Convert to uppercase for consistency
    else:
        print(f"Player {player} not found.")

# Example usage (optional, uncomment to test)
# play_word("player1", "TEST")
# update_point_totals()
# print(f"Updated Player Points: {player_to_points}")