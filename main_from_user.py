from plotter import Plotter
from category import Categorize  # this class includes the functions of pip and read csv


def main():
    plotter = Plotter()
    categorize = Categorize()

    print('read polygon.csv')

    (x_p, y_p, num_p) = categorize.csv_r('polygon.csv') # read csv

    plotter.add_polygon(x_p, y_p)

    print('Insert point information')
    try:
        x = float(input('x coordinate: '))
    except ValueError:
        print('Please enter right x coordinate')  # debug the value error
    else:
        try:
            y = float(input('y coordinate: '))
        except ValueError:
            print('Please enter right y coordinate')

        else:

            print('categorize point')
            kind = categorize.pip(x_p, y_p, x, y)  # get the kind of the point

            print('plot polygon and point')
            plotter.add_point(x, y, kind)
            plotter.show()


if __name__ == '__main__':
    main()
