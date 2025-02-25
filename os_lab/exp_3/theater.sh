#!/bin/bash

# Initialize arrays (queues)
online_queue=()
offline_queue=()

# Function to add booking requests to queues
add_request() {
    local queue_type=$1
    local customer_name=$2

    if [ "$queue_type" = "online" ]; then
        online_queue+=("$customer_name")
    elif [ "$queue_type" = "offline" ]; then
        offline_queue+=("$customer_name")
    fi
}

# Function to process booking requests
process_requests() {
    local seats_available=100  # Example: Total seats available

    # Process online requests first
    while [ ${#online_queue[@]} -gt 0 ] && [ $seats_available -gt 0 ]; do
        customer=${online_queue[0]}
        online_queue=("${online_queue[@]:1}")
        echo "Booking ticket for $customer..."
        ((seats_available--))
        echo "Remaining seats: $seats_available"
    done

    # Process offline requests
    while [ ${#offline_queue[@]} -gt 0 ] && [ $seats_available -gt 0 ]; do
        customer=${offline_queue[0]}
        offline_queue=("${offline_queue[@]:1}")
        echo "Booking ticket for $customer..."
        ((seats_available--))
        echo "Remaining seats: $seats_available"
    done

    # Check if there are remaining requests without seats
    if [ ${#online_queue[@]} -gt 0 ] || [ ${#offline_queue[@]} -gt 0 ]; then
        echo "No more seats available for the following customers:"
        for customer in "${online_queue[@]}"; do
            echo "$customer"
        done
        for customer in "${offline_queue[@]}"; do
            echo "$customer"
        done
    fi
}

# Example usage
echo "Adding booking requests..."
add_request "online" "John Doe"
add_request "online" "Jane Doe"
add_request "offline" "Bob Smith"
add_request "offline" "Alice Johnson"

echo "Processing booking requests..."
process_requests
