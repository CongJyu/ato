# encoding utf-8

import numpy as npy
import matplotlib.pyplot as plt
from numpy import polyfit


# draw/plot a line chart
def line_chart():
    print("Plot a line chart!")
    # basic settings
    pic_name = input("Name of picture: ")
    x_label = input("Name of x-axis: ")
    y_label = input("Name of y-axis: ")
    line_label = input("Name of line: ")
    # input array: x-axis and y-axis
    arr_x = input(x_label + " data: ")
    arr_y = input(y_label + " data: ")
    in_x = [float(count) for count in arr_x.split()]
    in_y = [float(count) for count in arr_y.split()]
    x = npy.array(in_x)
    y = npy.array(in_y)
    if len(x) != len(y):
        print("ERR! Length of x-axis and y-axis are not equal.")
    else:
        n = len(x)
        # console output messages
        print("Picture's name: %s, len of data: %d" % (pic_name, n))
        # plot settings
        plt.rcParams["figure.figsize"] = (10, 10)
        plt.subplots_adjust(left=0.06, right=0.94, top=0.92, bottom=0.08)
        plt.plot(x, y, label=line_label)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(pic_name)
        plt.legend()
        plt.show()
        #  messages
        print("Done!")


# fitting
def fitting():
    print("Optimize and plot a chart!")
    # basic settings
    pic_name = input("Name of picture: ")
    x_label = input("Name of x-axis: ")
    y_label = input("Name of y-axis: ")
    # input array: x-axis and y-axis
    arr_x = input(x_label + " data: ")
    arr_y = input(y_label + " data: ")
    in_x = [float(count) for count in arr_x.split()]
    in_y = [float(count) for count in arr_y.split()]
    x = npy.array(in_x)
    y = npy.array(in_y)
    # judge the length of x-axis and y-axis
    if len(x) != len(y):
        # not equal
        print("ERR! Length of x-axis and y-axis are not equal.")
    else:
        # conditions confirmed
        n = len(x)
        print("Picture's name: %s, len of data: %d" % (pic_name, n))
        # plot settings
        plt.rcParams["figure.figsize"] = (10, 10)
        plt.subplots_adjust(left=0.06, right=0.94, top=0.92, bottom=0.08)
        output_result = polyfit(x, y, 1)
        # console output message
        print(y_label, " = ", output_result[0], " * ", x_label, " + ", output_result[1])
        # generate picture
        plt.plot(x, output_result[0] * x + output_result[1], "k-")
        plt.plot(x, y, "b--")
        plt.show()
        # messages
        print("Done!")


# draw/plot a pie chart
# TODO: The explode of the pie chart, input methods.
def pie_chart():
    title = input("Input title: ")
    # labels and size input
    input_label = input("Input labels: ").split()
    input_size = input("Input size: ").split()
    input_colors = input("Input colors: ").split()
    # set the shadow of the pie chart
    while True:
        show_shadow = input("Show shadow?(0 or 1): ")
        if int(show_shadow) == 0:
            shadow = False
            break  # not display shadow
        elif int(show_shadow) == 1:
            shadow = True
            break  # display shadow
        else:
            # unexpected inputs
            print("You can only enter 0 or 1.")
    # input_explode = input("Input explode: ")
    labels = input_label
    size = input_size
    colors = input_colors
    # explode = (float(count) for count in input_explode.split())
    explode = (0.01, 0.01, 0.05)
    # judge the length of each arg
    if len(labels) != len(size):
        # labels are not equal to size
        print("ERR! Length of labels and size are not equal.")
    elif len(labels) != len(colors):
        # labels are not equal to colors
        print("ERR! Length of labels and colors are not equal.")
    elif len(size) != len(colors):
        # size are not equal to colors
        print("ERR! Length of size and colors are not equal.")
    else:
        # conditions confirmed
        plt.pie(
            size,
            explode=explode,
            labels=labels,
            colors=colors,
            labeldistance=1.2,
            autopct="%3.2f",
            shadow=shadow,
            startangle=90,
            pctdistance=0.6
        )
        plt.axis("equal")
        plt.title(title)  # show title
        plt.legend()  # show legend
        plt.show()


# find average
def average():
    print("Calculate average.")
    data = input("Input your data: ")
    input_data = [float(count) for count in data.split()]
    ave = (1 / len(input_data)) * npy.sum(input_data)
    print("Average is: ", ave)


def standard_deviation():
    print("Calculate standard deviation.")
    data = input("Input your data: ")
    input_data = [float(count) for count in data.split()]
    standard_deviation_output = npy.std(input_data)
    print("Standard deviation: ", standard_deviation_output)
