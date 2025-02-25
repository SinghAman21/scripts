#!/bin/bash

# Function to display menu
display_menu() {
    echo "Select an operation:"
    echo "1. Addition"
    echo "2. Subtraction"
    echo "3. Multiplication"
    echo "4. Division"
    echo "5. Modulus"
    echo "6. Exponentiation"
    echo "7. Exit"
}

# Function to perform calculations
perform_calculation() {
    local num1=$1
    local num2=$2
    local choice=$3

    case $choice in
        1) result=$(echo "$num1 + $num2" | bc);;
        2) result=$(echo "$num1 - $num2" | bc);;
        3) result=$(echo "$num1 * $num2" | bc);;
        4) if [ "$num2" != "0" ]; then
               result=$(echo "scale=2; $num1 / $num2" | bc)
           else
               echo "Error: Division by zero."
               return
           fi;;
        5) if [ "$num2" != "0" ]; then
               result=$(echo "$num1 % $num2" | bc)
           else
               echo "Error: Modulus by zero."
               return
           fi;;
        6) result=$(echo "e($num1 * l($num2))" | bc -l);;
    esac

    echo "Result: $result"
}

# Main loop
while true; do
    display_menu
    read -p "Enter your choice: " choice

    if [ "$choice" == "7" ]; then
        echo "Exiting..."
        break
    fi

    if [ "$choice" -lt "1" ] || [ "$choice" -gt "7" ]; then
        echo "Invalid choice. Please choose a valid option."
        continue
    fi

    read -p "Enter the first number: " num1
    read -p "Enter the second number: " num2

    # Validate input
    if ! [[ "$num1" =~ ^-?[0-9]+([.][0-9]+)?$ ]] || ! [[ "$num2" =~ ^-?[0-9]+([.][0-9]+)?$ ]]; then
        echo "Error: Invalid number(s) entered."
        continue
    fi

    perform_calculation "$num1" "$num2" "$choice"
done
