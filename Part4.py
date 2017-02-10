import Part3
import random


def histogram(data_list):
    sorted_list = sorted(data_list)
    start = 0
    length = len(sorted_list)

    ranges = [range(0, 10), range(10, 20), range(20, 30),
              range(30, 40), range(40, 50), range(50, 60),
              range(60, 70), range(70, 80), range(80, 90), range(90, 100)]

    index = start
    binned_list = []
    for num_range in ranges:
        temp_list = []
        while index < len(sorted_list) and sorted_list[index] in num_range:
            temp_list.append(sorted_list[index])
            index += 1
        if len(temp_list) == 0:
            binned_list.append(0)
        else:
            data_sum = 0
            for i in temp_list:
                data_sum += 1
            binned_list.append(data_sum)
    return binned_list


def write_histogram(data_list, file_stream):
    normalized_list = Part3.min_max(data_list, 0, 100)
    group = 0
    for i in range(0, len(normalized_list)):
        file_stream.write((str(group) + "-" + str(group + 9)).ljust(5) + "|" + ('*' * round(normalized_list[i])).ljust(101) + str(data_list[i]) + "\n")
        group += 10


def SRSWR(data_list, s):
    sample = []
    for i in range(0, s):
        sample.append(data_list[random.randint(0, len(data_list) - 1)])
    return sample


def SRSWOR(data_list, s):
    sample = []
    for i in range(0, s):
        index = random.randint(0, len(data_list))
        sample.append(data_list[index])
        data_list.pop(index)
    return sample


def stratified(data_list, s):
    sorted_list = sorted(data_list)
    young = range(0, 33)
    middle_aged = range(33, 60)

    young_list = []
    middle_aged_list = []
    old_list = []

    index = 0
    while sorted_list[index] in young:
        young_list.append(sorted_list[index])
        index += 1

    while sorted_list[index] in middle_aged:
        middle_aged_list.append(sorted_list[index])
        index += 1

    for i in range(index, len(sorted_list)):
        old_list.append(sorted_list[i])

    return [SRSWR(young_list, s), SRSWR(middle_aged_list, s), SRSWR(old_list, s)]
