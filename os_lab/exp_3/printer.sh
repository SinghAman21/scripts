#!/bin/bash

# Initialize arrays for job IDs and sizes
job_ids=()
job_sizes=()

# Function to add print jobs to the queue
add_job() {
    local job_id=$1
    local num_pages=$2

    job_ids+=("$job_id")
    job_sizes+=("$num_pages")
}

# Function to process print jobs
process_jobs() {
    # Combine job IDs and sizes into a single array for sorting
    for ((i=0; i<${#job_ids[@]}; i++)); do
        jobs+=("${job_sizes[$i]} ${job_ids[$i]}")
    done

    # Sort jobs based on size
    IFS=$'\n' sorted_jobs=($(sort -n <<<"${jobs[*]}"))

    # Process sorted jobs
    for job in "${sorted_jobs[@]}"; do
        read -r size id <<<"$job"
        echo "Printing Job ID: $id with $size pages."
        # Simulate printing time
        sleep 1  # Example delay to simulate printing
    done
}

# Example usage
echo "Adding print jobs..."
add_job "Job1" 10
add_job "Job2" 5
add_job "Job3" 20

echo "Processing print jobs..."
process_jobs
