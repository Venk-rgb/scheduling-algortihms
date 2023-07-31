from copy import deepcopy

from Process import get_process_details_with_priority, display_process_table_with_priority


def priority_scheduling_preemptive(process_list):
    ready_queue = [min(process_list, key=lambda process: process.arrival_time)]
    original_process_list = deepcopy(process_list)
    time = 0
    while len(ready_queue) > 0:
        current_process = ready_queue.pop(0)
        current_process.completion_time = time + 1
        current_process.burst_time -= 1
        current_process.turn_around_time = current_process.completion_time - current_process.arrival_time
        time += 1
        current_process.is_picked = True
        for i in range(len(process_list)):
            if process_list[i].arrival_time <= time and process_list[i].is_scheduled is False \
                    and process_list[i].is_picked is False:
                ready_queue.append(process_list[i])
                process_list[i].is_picked = True
        if current_process.burst_time == 0:
            current_process.is_scheduled = True
        else:
            ready_queue.append(current_process)
        ready_queue.sort(key=lambda x: (x.priority, x.arrival_time), reverse=False)
    for i in range(len(process_list)):
        process_list[i].wait_time = process_list[i].turn_around_time - original_process_list[i].burst_time
    display_process_table_with_priority(process_list)

process_list = get_process_details_with_priority()

priority_scheduling_preemptive(process_list)
