import Part1
import Part4

in_filename = input("Enter input file name: ")
out_filename = input("Enter output file name: ")
data_list = Part1.get_data(in_filename)
file_stream = open(out_filename, 'w')
s = int(input("Enter sample size"))

file_stream.write("Histogram:\n")
hist = Part4.histogram(data_list)
Part4.write_histogram(hist, file_stream)

file_stream.write("SRSWR\n")
file_stream.write(str(Part4.SRSWR(data_list, s)) + "\n")

file_stream.write("SRSWOR\n")
file_stream.write(str(Part4.SRSWOR(data_list, s)) + "\n")

file_stream.write("Stratified\n")
strat_list = Part4.stratified(data_list, s)
file_stream.write("Young: " + str(strat_list[0]) + "\n")
file_stream.write("Middle-age: " + str(strat_list[1]) + "\n")
file_stream.write("Old: " + str(strat_list[2]) + "\n")
