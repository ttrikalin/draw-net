from my_classes import * 
from my_functions import * 

StIndex = read_data("data.txt")
make_the_graph("L1.dot", StIndex[1], 0, True)
make_the_graph("L2.dot", StIndex[1], 1, True)




StIndex = read_data("ravi.txt")
make_the_graph("ravi.dot", StIndex[1], 0, True)
