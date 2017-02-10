def get_file_data(filename):
    data_list = [line.rstrip('\n') for line in open(filename)]
    new_list = []
    for i in data_list:
        new_list.append(list(map(lambda x: float(x), i.split(" "))))

    return data_list


def minchowski_distance(point1, point2, i):
    sum = 0
    for dimension in range(0, len(point1)):
        sum += abs((point1[dimension] - point2[dimension])) ** i
    return sum ** (1/i)


def supremum_distance(point1, point2):
    maximum = 0
    for i in range(0, len(point1)):
        distance = abs((point1[i] - point2[i]))
        if distance > maximum:
            maximum = distance
    return maximum


def cosine_similarty(A, B):
    dividend = 0
    for i in range(0, len(A)):
        dividend += A[i] * B[i]

    sum1 = 0
    for i in range(0, len(A)):
        sum1 += A[i] ** 2

    sum2 = 0
    for i in range(0, len(A)):
        sum2 += B[i] ** 2

    return dividend/((sum1**0.5)*(sum2**0.5))
