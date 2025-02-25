#!/bin/bash

# Function to perform calculations
calculate() {
    local num1=$1
    local num2=$2
    local operator=$3

    case $operator in
        "+") result=$((num1 + num2));;
        "-") result=$((num1 - num2));;
        "*") result=$((num1 * num2));;
        "/") 
            if [ $num2 -eq 0 ]; then
                result="Error: Division by zero"
            else
                result=$(( num1 / num2))
            fi
            ;;
        *) result="Invalid operator";;
    esac

    echo "$result"
}

# Get user input
read -p "Enter the first number: " num1
read -p "Enter the operator (+, -, *, /): " operator
read -p "Enter the second number: " num2

# Validate input
if ! [[ "$num1" =~ ^-?[0-9]+([.][0-9]+)?$ ]] || ! [[ "$num2" =~ ^-?[0-9]+([.][0-9]+)?$ ]]; then
    echo "Error: Invalid number(s) entered."
    exit 1
fi

# Perform the calculation
result=$(calculate "$num1" "$num2" "$operator")

echo "Result: $result"
