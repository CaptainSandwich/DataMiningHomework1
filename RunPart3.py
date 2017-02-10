import Part1
import Part3

in_filename = input("Enter input file name: ")
out_filename = input("Enter output file name: ")
data_list = Part1.get_data(in_filename)
file_stream = open(out_filename, 'w')
new_min = float(input("Enter new min: "))
new_max = float(input("Enter new max: "))

file_stream.write("Data min-max normalized:\n")
file_stream.write(str(Part3.min_max(data_list, new_min, new_max)) + "\n")

file_stream.write("Data z-score normalized:\n")
file_stream.write(str(Part3.z_score(data_list)) + "\n")

file_stream.write("Data decimal scaled:\n")
file_stream.write(str(Part3.decimal_scaling(data_list)) + "\n")
