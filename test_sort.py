import random
import time

N = 100
random.seed(int(time.time()))

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
    # raise NotImplementedError

# Do not change the following lines
def test_insertion_sort():
    input_list = list(range(N))
    random.shuffle(input_list)
    output_list = insertion_sort(input_list)
    assert output_list == sorted(output_list), "Input list is not sorted"

def test_reference():
    input_list = list(range(N))
    random.shuffle(input_list)
    output_list = sorted(input_list)
    assert output_list == sorted(output_list), "Input list is not sorted"


if __name__ == "__main__":
    test_insertion_sort()
    test_reference()
    print("All tests passed")