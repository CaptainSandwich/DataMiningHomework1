from functools import reduce

def get_data(file_name):
    try:
        file_stream = open(file_name, 'r')
    except IOError:
        print("Error: can\'t find file or read data")
        return None
    data = file_stream.read()
    file_stream.close()
    if len(data) <= 0:
        print("Error: file empty")
        return None
    parsed_strings = data.split(', ')
    parsed_ints = list(map(int, parsed_strings))
    return parsed_ints


def get_mean(data_list):
    try:
        data_sum = reduce((lambda x, y: x + y), data_list)
    except TypeError:
        print("Error: cannot find average of empty list")
        return None
    mean = data_sum / len(data_list)
    return mean


def get_midrange(data_list):
    try:
        return (min(data_list) + max(data_list))/2
    except ValueError:
        print("Error: cannot find midrange of empty list")
        return None


def get_median(data_list):
    length = len(data_list)
    if length % 2 == 1:
        return data_list[length//2]
    else:
        return (data_list[(length-1)//2] + data_list[(length//2)])/2.0


def get_q1(data_list):
    length = len(data_list)//2
    first_half = data_list[0:length]
    return get_median(first_half)


def get_q3(data_list):
    length = len(data_list)
    second_half = data_list[length//2 + length % 2:]
    return get_median(second_half)


def get_mode(data_list):
    nums = {}
    modes = []
    for i in data_list:
        if str(i) in nums:
            nums[str(i)] += 1
        else:
            nums[str(i)] = 1
    num = max(nums.values())
    for i in nums:
        if nums[i] == num:
            modes.append(int(i))
    if len(modes) == 1:
        modality = "unimodal"
    elif len(modes) == 2:
        modality = "bimodal"
    elif len(modes) == 3:
        modality = "trimodal"
    else:
        modality = "multimodal"
    return [modality, sorted(modes)]

