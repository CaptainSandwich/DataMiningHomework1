import Part1
import Part2

in_filename = input("Enter input file name: ")
out_filename = input("Enter output file name: ")
data_list = Part1.get_data(in_filename)
file_stream = open(out_filename, 'w')
depth = int(input("Enter bin depth: "))
width = int(input("Enter bin width: "))
l = int(input("Enter lower bound: "))
r = int(input("Enter upper bound: "))

file_stream.write("Equal depth bin means, k = " + str(depth) + "\n")
file_stream.write(str(Part2.equal_depth_means(data_list, depth)) + "\n")

file_stream.write("Equal depth bin boundaries, k = " + str(depth) + "\n")
file_stream.write(str(Part2.equal_depth_boundaries(data_list, depth)) + "\n")

file_stream.write("Equal width bin medians, d = " + str(width) + ", l = " + str(l) + " ,r = " + str(r) + "\n")
file_stream.write(str(Part2.equal_width_median(data_list, width, l, r)) + "\n")
