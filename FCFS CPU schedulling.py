# Define a Process class to hold process attributes
class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
def fcfs_scheduling(processes):
    # Initialize the start time of the first process to its arrival time
    start_time = processes[0].arrival_time
    total_wait_time = 0
    total_turnaround_time = 0

    print("Process ID\tArrival Time\tBurst Time\tStart Time\tEnd Time\tWait Time\tTurnaround Time")

    # Loop through each process in the list of processes
    for process in processes:
        # Calculate the end time of the current process
        end_time = start_time + process.burst_time
        # Calculate the wait time and turnaround time of the current process
        wait_time = start_time - process.arrival_time
        turnaround_time = end_time - process.arrival_time

        # Print the process details
        print(f"{process.process_id}\t\t{process.arrival_time}\t\t{process.burst_time}\t\t{start_time}\t\t{end_time}\t\t{wait_time}\t\t{turnaround_time}")

        # Add the wait time and turnaround time of the current process to the totals
        total_wait_time += wait_time
        total_turnaround_time += turnaround_time

        # Set the start time of the next process to the end time of the current process
        start_time = end_time

    # Calculate the average wait time and average turnaround time of all processes
    avg_wait_time = total_wait_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    # Print the average wait time and average turnaround time
    print(f"\nAverage Wait Time: {avg_wait_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# Define the main function to create and run the processes


def main():
    # Create a list of three processes with different arrival times and burst times
    processes = [
        Process(1, 0, 8),
        Process(2, 1, 4),
        Process(3, 2, 9)
    ]

    # Call the FCFS scheduling function with the list of processes
    fcfs_scheduling(processes)


# Call the main function to run the program
if __name__ == '__main__':
    main()