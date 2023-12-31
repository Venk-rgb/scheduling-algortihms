class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turn_around_time = 0
        self.priority = priority
        self.wait_time = 0
        self.is_scheduled = False
        self.is_picked = False


def display_process_table(process_list):
    process_list.sort(key=lambda x: x.pid, reverse=False)
    print("PID  AT  BT  CT  TAT  WT")
    total_wait_time = 0
    total_turn_around_time = 0
    for i in range(len(process_list)):
        print("P" + str(process_list[i].pid), end="   ")
        print(process_list[i].arrival_time, end="   ")
        print(process_list[i].burst_time, end="   ")
        print(process_list[i].completion_time, end="   ")
        print(process_list[i].turn_around_time, end="  ")
        print(process_list[i].wait_time)
        total_wait_time += process_list[i].wait_time
        total_turn_around_time += process_list[i].turn_around_time
    print("Average wait time = ", (total_wait_time / len(process_list)))
    print("Average turn around time = ", (total_turn_around_time / len(process_list)))


def display_process_table_with_priority(process_list):
    process_list.sort(key=lambda x: x.pid, reverse=False)
    print("PID  AT  BT  Pr  CT  TAT  WT")
    for i in range(len(process_list)):
        print("P" + str(process_list[i].pid), end="   ")
        print(process_list[i].arrival_time, end="   ")
        print(process_list[i].burst_time, end="   ")
        print(process_list[i].priority, end="   ")
        print(process_list[i].completion_time, end="   ")
        print(process_list[i].turn_around_time, end="  ")
        print(process_list[i].wait_time)


def get_process_details():
    number_of_processes = int(input("Enter number of processes: "))
    process_list = []
    for i in range(number_of_processes):
        pid = int(input("Enter process id: "))
        arrival_time = int(input("Enter arrival time: "))
        burst_time = int(input("Enter burst time: "))
        process_list.append(Process(pid, arrival_time, burst_time, 0))
    return process_list


def get_process_details_with_priority():
    number_of_processes = int(input("Enter number of processes: "))
    process_list = []
    for i in range(number_of_processes):
        pid = int(input("Enter process id: "))
        arrival_time = int(input("Enter arrival time: "))
        burst_time = int(input("Enter burst time: "))
        priority = int(input("Enter priority: "))
        process_list.append(Process(pid, arrival_time, burst_time, priority))
    return process_list
