#!/bin/bash

# Generate a random number between 1 and 100
secret_number=$(( (RANDOM % 100) + 1 ))

echo "Welcome to the Guessing Game!"

while true; do
    # Ask the user to guess the number
    read -p "Enter your guess (1-100): " user_guess

    # Validate the input
    if ! [[ "$user_guess" =~ ^[1-9][0-9]?$|^100$ ]]; then
        echo "Please enter a valid number between 1 and 100."
        continue
    fi

    # Check if the guess is correct
    if [ "$user_guess" -eq "$secret_number" ]; then
        echo "Congratulations! You guessed the correct number."
        break
    elif [ "$user_guess" -lt "$secret_number" ]; then
        echo "Try a higher number."
    else
        echo "Try a lower number."
    fi
done
