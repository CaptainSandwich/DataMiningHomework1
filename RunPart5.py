import Part5
filename = input("Enter an input file path: ")
data_list = Part5.get_file_data(filename)
data_list.pop(0)
out_filename = input("Enter an output file path:")
file_stream = open(out_filename, 'w')
point_string = input("Enter a space separated point: ")
point = list(map(lambda x: float(x), point_string.split(" ")))
col1 = int(input("Enter index of first column for covariance: "))
col2 = int(input("Enter index second column for covariance: "))
file_stream.write("Euclidean distances:\n")
for i in data_list:
    file_stream.write("%.4f\n" % Part5.minkowski_distance(point, i, 2))

file_stream.write("Manhattan distances:\n")
for i in data_list:
    file_stream.write("%.4f\n" % Part5.minkowski_distance(point, i, 1))

file_stream.write("Supremum distances:\n")
for i in data_list:
    file_stream.write("%.4f\n" % Part5.supremum_distance(point, i))

file_stream.write("Cosine similarity:\n")
for i in data_list:
    file_stream.write("%.4f\n" % Part5.cosine_similarity(point, i))

file_stream.write("Covariance between column " + str(col1) + " and " + str(col2) + "\n")
file_stream.write("%.4f\n" % Part5.covariance(data_list, col1, col2))

file_stream.write("Correlation coefficient between column " + str(col1) + " and " + str(col2) + "\n")
file_stream.write("%.4f\n" % Part5.correlation_coefficient(data_list, col1, col2))
