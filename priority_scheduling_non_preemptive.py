from Process import get_process_details_with_priority, display_process_table_with_priority


def priority_scheduling_non_preemptive(process_list):
    process_list.sort(key=lambda x: x.arrival_time, reverse=False)
    completion_time = 0
    time = 0
    while any(process.is_scheduled is False for process in process_list):
        available_processes = [process for process in process_list if
                               process.arrival_time <= time and process.is_scheduled is False]
        if len(available_processes) == 0:
            time += 1
            continue
        available_processes.sort(key=lambda x: x.priority, reverse=False)
        completion_time = completion_time + available_processes[0].burst_time
        available_processes[0].completion_time = completion_time
        available_processes[0].turn_around_time = available_processes[0].completion_time - available_processes[
            0].arrival_time
        available_processes[0].wait_time = available_processes[0].turn_around_time - available_processes[0].burst_time
        available_processes[0].is_scheduled = True
        time += available_processes[0].burst_time

    display_process_table_with_priority(process_list)


process_list = get_process_details_with_priority()

priority_scheduling_non_preemptive(process_list)