from typing import List

def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    left, right = max(newspapers_read_times), sum(newspapers_read_times)
    boundary_index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if get_number_of_needed_workers(newspapers_read_times, mid) <= num_coworkers:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

def get_number_of_needed_workers(read_times: List[int], limit: int) -> int:
    workers = 1
    time = 0

    for read_time in read_times:
        if time + read_time > limit:
            workers += 1
            time = read_time
        else:
            time += read_time

    return workers
