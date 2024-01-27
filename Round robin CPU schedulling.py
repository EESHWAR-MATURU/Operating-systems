# Define a Process class to hold process attributes
class Process:
    def __init__(self, process_id, burst_time):
        self.process_id = process_id
        self.burst_time = burst_time
        self.remaining_time = burst_time

# Define a function to implement Round Robin scheduling algorithm


def round_robin_scheduling(processes, quantum):
    n = len(processes)
    wait_time = [0] * n
    turnaround_time = [0] * n
    total_wait_time = 0
    total_turnaround_time = 0
    time = 0

    while True:
        all_done = True

        for i in range(n):
            if processes[i].remaining_time > 0:
                all_done = False

                if processes[i].remaining_time > quantum:
                    time += quantum
                    processes[i].remaining_time -= quantum
                else:
                    time += processes[i].remaining_time
                    wait_time[i] = time - processes[i].burst_time
                    processes[i].remaining_time = 0
                    turnaround_time[i] = time

        if all_done:
            break

    print("Process ID\tBurst Time\tWait Time\tTurnaround Time")

    for i in range(n):
        total_wait_time += wait_time[i]
        total_turnaround_time += turnaround_time[i]
        print(
            f"{processes[i].process_id}\t\t{processes[i].burst_time}\t\t{wait_time[i]}\t\t{turnaround_time[i]}")

    # Calculate the average wait time and average turnaround time of all processes
    avg_wait_time = total_wait_time / n
    avg_turnaround_time = total_turnaround_time / n

    # Print the average wait time and average turnaround time
    print(f"\nAverage Wait Time: {avg_wait_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# Define the main function to create and run the processes


def main():
    # Create a list of four processes with different burst times
    processes = [
        Process(1, 6),
        Process(2, 8),
        Process(3, 7),
        Process(4, 3)
    ]

    # Call the Round Robin scheduling function with the list of processes and quantum time of 3
    round_robin_scheduling(processes, 3)


# Call the main function to run the program
if __name__ == '__main__':
    main()
