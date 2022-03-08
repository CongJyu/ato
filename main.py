import numpy as npy
import matplotlib.pyplot as plt


#  draw/plot a line chart
def line_chart():
    print("Plot a line chart!")
    #  basic settings
    pic_name = input("Name of picture: ")
    x_label = input("Name of x-axis: ")
    y_label = input("Name of y-axis: ")
    #  How to input Numpy array?
    x = npy.array([0.0, 3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0])
    y = npy.array([16.50, 18.55, 20.60, 22.95, 25.15, 27.20, 29.40, 31.50])
    n = len(x)
    print("Picture's name: %s, len of data: %d" % (pic_name, n))
    plt.rcParams["figure.figsize"] = (10, 10)
    plt.subplots_adjust(left=0.06, right=0.94, top=0.92, bottom=0.08)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x, y, label="")
    plt.show()


#  main process
if __name__ == "__main__":
    print("Welcome use ato!")
    print("Alternative To OriginLab!")
    while 1:
        command = input("ato >>> ")
        if command == "quit":
            #  this command is used to quit this CLI
            print("Thank you for using ato! Bye!")
            quit(0)
        elif command == "help":
            #  help and information
            print("---- ato Help ----")
        elif command == "line-chart":
            #  draw/plot a line chart
            line_chart()
