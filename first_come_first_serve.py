from Process import display_process_table, get_process_details


def first_come_first_serve(process_list):
    process_list.sort(key=lambda x: x.arrival_time, reverse=False)
    completion_time = 0
    time = 0
    i = 0
    while i < len(process_list):
        if time < process_list[i].arrival_time:
            time += 1
            completion_time += 1
            continue
        completion_time = completion_time + process_list[i].burst_time
        process_list[i].completion_time = completion_time
        process_list[i].turn_around_time = process_list[i].completion_time - process_list[i].arrival_time
        process_list[i].wait_time = process_list[i].turn_around_time - process_list[i].burst_time
        time += process_list[i].burst_time
        i += 1

    display_process_table(process_list)


process_list = get_process_details()

first_come_first_serve(process_list)
