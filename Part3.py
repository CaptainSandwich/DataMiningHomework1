import Part1
def min_max(data_list, new_min, new_max):
    old_min = min(data_list)
    old_max = max(data_list)
    new_list = []
    for i in data_list:
        new_list.append((((i - old_min)/(old_max - old_min))*(new_max - new_min)) + new_min)
    return new_list


def z_score(data_list):
    mean = Part1.get_mean(data_list)
    sum = 0
    for i in data_list:
        sum += ((i - mean)**2)
    variance = sum/len(data_list)
    standard_deviation = variance**0.5
    new_list = []
    for i in data_list:
        new_list.append((i - mean)/standard_deviation)
    return new_list


def decimal_scaling(data_list):
    max_val = max(abs(min(data_list)), abs(max(data_list)))
    i = 0
    while max_val/(10**i) >= 1:
        i += 1
    return list(map(lambda x: x/(10**i), data_list))