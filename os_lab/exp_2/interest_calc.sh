#!/bin/bash

# Function to clear the screen
clear_screen() {
    clear
}

# Function to display the main menu
display_menu() {
    echo -e "\n\t\t              Simple Interest Calculator\n"
    echo -e "\t------------------------------------------------------------------------------\n"
}

# Function to calculate simple interest
calculate_interest() {
    local principal=$1
    local rate=$2
    local time=$3

    # Use awk for floating-point calculations
    local interest=$(awk "BEGIN {print ($principal * $rate * $time) / 100}")
    local total_amount=$(awk "BEGIN {print $principal + ($principal * $rate * $time) / 100}")

    echo -e "\n\tInterest: \t$interest"
    echo -e "\tTotal Amount: \t$total_amount"
}

# Main loop
while true; do
    clear_screen
    display_menu

    read -p "Enter the Principal Amount: " principal
    read -p "Enter the Interest Rate (in %): " rate
    read -p "Enter the Time (in years): " time

    # Validate input
    if ! [[ "$principal" =~ ^[0-9]+([.][0-9]+)?$ ]] || ! [[ "$rate" =~ ^[0-9]+([.][0-9]+)?$ ]] || ! [[ "$time" =~ ^[0-9]+([.][0-9]+)?$ ]]; then
        echo "Error: Invalid input. Please enter valid numbers."
        read -p "Press Enter to continue..."
        continue
    fi

    # Calculate and display interest
    echo -e "\n\tCalculation Results:"
    calculate_interest "$principal" "$rate" "$time"

    # Ask if user wants to continue
    read -p "Do you want to continue? (y/n): " choice
    case $choice in
        y|Y) continue ;;
        n|N) echo "Exiting..."; exit 0 ;;
        *) echo "Invalid choice. Exiting..."; exit 1 ;;
    esac
done
