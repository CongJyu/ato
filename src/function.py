import numpy as npy
import matplotlib.pyplot as plt


#  draw/plot a line chart
def line_chart():
    print("Plot a line chart!")
    #  basic settings
    pic_name = input("Name of picture: ")
    x_label = input("Name of x-axis: ")
    y_label = input("Name of y-axis: ")
    #  input array: x-axis and y-axis
    arr_x = input(x_label + " data: ")
    arr_y = input(y_label + " data: ")
    in_x = [float(count) for count in arr_x.split()]
    in_y = [float(count) for count in arr_y.split()]
    x = npy.array(in_x)
    y = npy.array(in_y)
    n = len(x)
    print("Picture's name: %s, len of data: %d" % (pic_name, n))
    #  plot settings
    plt.rcParams["figure.figsize"] = (10, 10)
    plt.subplots_adjust(left=0.06, right=0.94, top=0.92, bottom=0.08)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x, y, label="")
    plt.show()
    #  messages
    print("Done!")
