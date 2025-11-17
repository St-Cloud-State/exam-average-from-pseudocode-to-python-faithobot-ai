"""
Full Name: Faith Obot
Class-Section: IS 250-01
Assignment Title: Calculate Average of Three Scores
Submission Date: November /06/2025
"""
"""
Ask the user to enter the first exam score.
Ask the user to enter the second exam score.
Ask the user to enter the third exam score.
Convert all three inputs to integers.
Create a function named calculate_average.
Inside the function, add the three scores and divide by 3 to get the average.
Print each of the three scores on its own line.
Print the average score on its own line.
"""

# Your Python code begins below this line.
# Every line you write must have a comment directly above it.

 # Define a function that will calculate and print the average of three scores
def calculate_average():
     # Ask the user for the first exam score
    first_score = int(input("Enter first exam score: "))

     # Ask the user for the second exam score
    second_score = int(input("Enter second exam score: "))

     # Ask the user for the third exam score
    third_score = int(input("Enter third exam score: "))

     # Calculate the average of the three scores
    average_score = (first_score + second_score + third_score) / 3

     # Print the first score on its own line
    print("First score:", first_score)

     # Print the second score on its own line
    print("Second score:", second_score)

     # Print the third score on its own line
    print("Third score:", third_score)

     # Print the average score
    print("The average score is:", average_score)

# Call your function when your program is ready
calculate_average()   
  
