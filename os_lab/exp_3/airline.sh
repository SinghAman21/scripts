#!/bin/bash

# Initialize arrays for passenger classes
high_priority=()
medium_priority=()
low_priority=()

# Function to add passengers to their respective queues
add_passenger() {
    local passenger_class=$1
    local passenger_name=$2
    local checkin_time=$3

    if [ "$passenger_class" = "high" ]; then
        high_priority+=("$passenger_name $checkin_time")
    elif [ "$passenger_class" = "medium" ]; then
        medium_priority+=("$passenger_name $checkin_time")
    elif [ "$passenger_class" = "low" ]; then
        low_priority+=("$passenger_name $checkin_time")
    fi
}

# Function to process passengers
process_passengers() {
    # Process high-priority passengers first
    echo "Processing High-Priority Passengers:"
    for passenger in "${high_priority[@]}"; do
        read -r name time <<<"$passenger"
        echo "Checking in $name..."
        sleep 1  # Simulate check-in time
        echo "Check-in completed for $name."
    done

    # Process medium-priority passengers next
    echo "Processing Medium-Priority Passengers:"
    for passenger in "${medium_priority[@]}"; do
        read -r name time <<<"$passenger"
        echo "Checking in $name..."
        sleep 1  # Simulate check-in time
        echo "Check-in completed for $name."
    done

    # Process low-priority passengers last
    echo "Processing Low-Priority Passengers:"
    for passenger in "${low_priority[@]}"; do
        read -r name time <<<"$passenger"
        echo "Checking in $name..."
        sleep 1  # Simulate check-in time
        echo "Check-in completed for $name."
    done
}

# Example usage
echo "Adding passengers..."
add_passenger "medium" "Alice Brown" 2
add_passenger "high" "Jane Smith" 3
add_passenger "medium" "Bob Johnson" 1
add_passenger "high" "John Doe" 2
add_passenger "low" "Mike Davis" 4
add_passenger "low" "Emily Taylor" 1

echo "Processing passengers..."
process_passengers
