# scheduling-algortihms
Python repository containing implementation of all OS scheduling algorithms.
The goal is to implement the popular CPU scheduling algorithms in python. 

The various algorithms implemented are:
1. First Come First Serve
2. Shortest Job First (Preemptive and Non-Preemptive)
3. Priority Scheduling (Non-Preemptive)
4. Round Robing Scheduling

### First Come First Serve 
In First Come First Serve (FCFS) scheduling, computer processes are executed in the order they arrive in the ready queue. The process that arrives first gets executed first, and the CPU continues executing processes in the order they appeared, without preemption, until each process completes its execution. While FCFS is simple to implement, it may lead to inefficient CPU utilization and longer waiting times, as longer processes can delay the execution of shorter ones, making it less suitable for scenarios with varying execution times.

### Shortest Job First Non-Preemptive
Shortest Job First Non-Preemptive (SJF-NP) is a CPU scheduling algorithm that prioritizes the shortest burst time (execution time) for processes, without preemption. When a set of processes is ready for execution, the CPU selects the process with the shortest burst time and runs it until it completes its execution. Only when the running process finishes or is blocked for an I/O operation does the CPU move on to the next process with the shortest burst time from the remaining processes. SJF Non-Preemptive can lead to optimal average waiting times for processes when the burst times are known in advance, as it allows the shortest tasks to be executed first. However, it may not be as effective in situations where burst times are unpredictable or dynamic, as it cannot adapt to newer, shorter processes that may arrive after the scheduling has started.

### Shortest Job First Preemptive
In SJF Preemptive, the CPU selects the process with the shortest burst time (time needed to complete its execution) among the available processes. If a new process with a shorter burst time arrives while a process is already running, the CPU may preempt (pause) the currently running process and start executing the new shorter one. This preemption allows the system to prioritize shorter processes, reducing waiting times for all processes. SJF Preemptive is particularly useful when the burst times of processes are known in advance, as it requires knowledge of the expected execution time for accurate scheduling decisions. However, it may not be as suitable for real-time systems or situations where process execution times are not well-defined or unpredictable.

### Priority Scheduling Non-Preemptive
Priority Scheduling Non-Preemptive is a CPU scheduling algorithm where each process is assigned a priority, and the CPU executes the process with the highest priority first. The priority can be determined based on various factors, such as the process's importance, deadline, or resource requirements. Once a process is selected for execution, it continues until it completes its execution or gets blocked for an I/O operation. The CPU then moves on to the next process with the highest priority from the remaining processes. Priority Scheduling Non-Preemptive can lead to efficient handling of important or time-sensitive tasks, but it may suffer from a potential "starvation" problem, where low-priority processes may never get a chance to execute if high-priority processes keep arriving. Proper priority assignment and aging mechanisms can be employed to mitigate this issue and ensure a fair distribution of CPU time among all processes.

### Round Robin 
Round Robin (RR) scheduling is a CPU scheduling algorithm where processes are executed in a circular manner based on fixed time slices or time quanta. Each process is given a limited amount of time to run (time quantum), and if it doesn't complete within that time, it is pre-empted, and the next process in the queue is given a chance to run. The pre-empted process is placed back at the end of the queue to await its turn again. RR provides fair sharing of CPU time among processes and ensures responsiveness, making it suitable for time-sharing systems, but the efficiency depends on the choice of the time quantum. Short time quanta enhance responsiveness but may increase context-switch overhead, while longer ones may lead to decreased fairness and responsiveness.

