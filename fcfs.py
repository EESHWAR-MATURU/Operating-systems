import time


def process_fcfs(processes):
    print("First-Come, First-Served (FCFS) Scheduling")
    waiting_time = 0
    response_time = 0
    turn_around_time = 0
    n = len(processes)

    for i in range(n):
        waiting_time += processes[i][1]
        response_time += processes[i][2] - processes[i][1]
        turn_around_time += processes[i][3] - processes[i][1]
        print("Process: ", processes[i][0], "\nBurst Time: ", processes[i][2] - processes[i][1],
              "\nWaiting Time: ", processes[i][1], "\nTurn-Around Time: ", processes[i][3] - processes[i][1])

    print("\nAverage Waiting Time: ", waiting_time / n)
    print("Average Response Time: ", response_time / n)
    print("Average Turn-Around Time: ", turn_around_time / n)


processes = [["P1", 0, 4, 4],
             ["P2", 1, 5, 6],
             ["P3", 2, 2, 4],
             ["P4", 3, 1, 4]]

process_fcfs(processes)
