from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt

# if plotting does not work comment the following line
matplotlib.use('qt5Agg')


class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_t_polygon(self, xs, ys, kind=None):  # for creativity to add the test polygon
        if kind == 'not inside':
            plt.fill(xs, ys, 'ro', label='not inside')

        elif kind == 'inside':
            plt.fill(xs, ys, 'go', label='inside')

    def add_point(self, x, y, kind=None):
        if kind == 'outside':
            plt.plot(x, y, 'ro', label='Outside')
        elif kind == 'boundary':
            plt.plot(x, y, 'bo', label='Boundary')
        elif kind == 'inside':
            plt.plot(x, y, 'go', label='Inside')
        else:
            plt.plot(x, y, 'ko', label='Unclassified')

    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.xlabel('x axis')
        plt.ylabel('y axis')     # add the axis label
        plt.title('Point-in-Polygon Test')   # add the title
        plt.show()

    def show_po(self):  # For creativity, which changed the title
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.xlabel('x axis')
        plt.ylabel('y axis')     # add the axis label
        plt.title('Polygon-in-Polygon Test')   # add the title
        plt.show()
