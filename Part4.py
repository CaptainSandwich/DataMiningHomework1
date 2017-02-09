import Part3


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


def print_histogram(data_list):
    normalized_list = Part3.min_max(data_list, 0, 100)
    group = 0
    for i in range(0, len(normalized_list)):
        print((str(group) + "-" + str(group + 9)).ljust(5) + "|" + ('*' * round(normalized_list[i])).ljust(101) + str(data_list[i]))
        group += 10

