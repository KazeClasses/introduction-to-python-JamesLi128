def insertion_sort(unsorted_list: list[int]) -> list[int]:
    # Implement your function here ...
    for crnt_idx, crnt_value in enumerate(unsorted_list[1:]):
        crnt_idx += 1
        for i in list(range(crnt_idx))[::-1]:
            if crnt_value < unsorted_list[i]:
                unsorted_list[crnt_idx] = unsorted_list[i]
                unsorted_list[i] = crnt_value
                crnt_idx -= 1
    return unsorted_list