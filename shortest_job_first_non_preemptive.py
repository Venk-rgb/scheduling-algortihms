from Process import get_process_details, display_process_table


def shortest_job_first_non_preemptive(process_list):
    process_list.sort(key=lambda x: x.arrival_time, reverse=False)
    time = 0
    completion_time = 0
    while any(process.is_scheduled is False for process in process_list):
        available_processes = [process for process in process_list if
                               process.arrival_time <= time and process.is_scheduled is False]
        if len(available_processes) == 0:
            time += 1
            continue
        available_processes.sort(key=lambda x: x.burst_time, reverse=False)
        completion_time = completion_time + available_processes[0].burst_time
        available_processes[0].completion_time = completion_time
        available_processes[0].turn_around_time = available_processes[0].completion_time - available_processes[
            0].arrival_time
        available_processes[0].wait_time = available_processes[0].turn_around_time - available_processes[0].burst_time
        available_processes[0].is_scheduled = True
        time += available_processes[0].burst_time

    display_process_table(process_list)


process_list = get_process_details()
shortest_job_first_non_preemptive(process_list)
