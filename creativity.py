"""
This program is trying to test whether a polygon is in another polygon.
there are three different situations are divided, which are inside and not inside.
What should be noticed is that the method should only work for Convex Polygons. If the polygons are not
convex, the methods can't work.
"""
from plotter import Plotter
from category import Categorize, Polygon  # this class includes the functions of pip and read csv


def main():
    plotter = Plotter()
    categorize = Categorize()
    polygon = Polygon()

    print('read polygon1.csv')

    (x_p, y_p, num_p) = categorize.csv_r('polygon1.csv')  # Use the new function in categorize to read csv

    plotter.add_polygon(x_p, y_p)  # Use the plotter to plot polygon

    print('read test_polygon.csv')

    (x_pt, y_pt, num_pt) = categorize.csv_r('test_polygon.csv')  # Use the function in categorize to read csv

    kinds_p = []
    for i in range(len(x_pt)):
        kinds_p.append(polygon.pip(x_p, y_p, x_pt[i], y_pt[i]))
    if 'outside' not in kinds_p:
        kind = 'inside'
    else:
        kind = 'not inside'

    print("the polygon is "+kind)
    plotter.add_t_polygon(x_pt, y_pt, kind)

    # The categorizing of test polygon, get the kind, plot the test polygon

    plotter.show()


if __name__ == '__main__':
    main()
