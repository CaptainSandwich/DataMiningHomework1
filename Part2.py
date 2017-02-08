import Part1
def equal_depth_means(data_list, k):
    sorted_list = sorted(data_list)
    binned_list = [sorted_list[i:i+k] for i in range(0, len(sorted_list), k)]
    for i in range(0, len(binned_list)):
        mean = Part1.get_mean(binned_list[i])
        for j in range(0, len(binned_list[i])):
            binned_list[i][j] = mean

    return binned_list