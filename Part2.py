import Part1


def equal_depth_means(data_list, k):
    sorted_list = sorted(data_list)
    binned_list = [sorted_list[i:i+k] for i in range(0, len(sorted_list), k)]

    for i in range(0, len(binned_list)):
        mean = Part1.get_mean(binned_list[i])
        for j in range(0, len(binned_list[i])):
            binned_list[i][j] = mean

    return binned_list


def equal_depth_boundaries(data_list, k):
    sorted_list = sorted(data_list)
    binned_list = [sorted_list[i:i+k] for i in range(0, len(sorted_list), k)]
    for i in range(0, len(binned_list)):
        for j in range(0, len(binned_list[i])):
            if abs(binned_list[i][j] - min(binned_list[i])) < abs(binned_list[i][j] - max(binned_list[i])):
                boundary = min(binned_list[i])
            else:
                boundary = max(binned_list[i])
            binned_list[i][j] = boundary

    return binned_list


def get_ranges(d, l, r):
    dividend = (r - l)//d
    ranges = [range(i, i + d) for i in range(l, l + (d * dividend), d)]
    ranges.append(range(l + (d * dividend), r + 1))
    return ranges


def equal_width_median(data_list, d, l, r):
    sorted_list = sorted(data_list)
    start = 0
    length = len(sorted_list)
    while start < length and sorted_list[start] < l:
        start += 1

    end = start
    while end < length and sorted_list[end] < r:
        end += 1

    ranges = get_ranges(d, l, r)

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
            binned_list.append(Part1.get_median(temp_list))
    return binned_list