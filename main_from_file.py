from plotter import Plotter
from category import Categorize, Polygon  # this class includes the functions of pip and read csv


def main():
    plotter = Plotter()
    categorize = Categorize()
    polygon = Polygon()

    print('read polygon.csv')

    (x_p, y_p, num_p) = categorize.csv_r('polygon.csv')    # Use the new function in categorize to read csv

    plotter.add_polygon(x_p, y_p)     # Use the plotter to plot polygon

    print('read input.csv')

    (x_pt, y_pt, num_pt) = categorize.csv_r('input.csv')  # Use the function in categorize to read csv

    print('categorize points')
    kinds = []       # is used to store the categorize information

    for i in range(len(x_pt)):
        kind = (polygon.pip(x_p, y_p, x_pt[i], y_pt[i]))
        plotter.add_point(x_pt[i], y_pt[i], kind)
        kinds.append(kind)
    # The categorizing of points, adding to list amd plot is done in one for statement

    print('write output.csv')

    with open('output.csv', 'w') as f:

        f.write('id,category\n')
        # write the information line which is not included in data, \n is used to change line

        for i in range(len(x_pt)):    # write the other data
            output = str(i + 1) + ',' + kinds[i] + '\n'
            # the first column is the ID and the second column is the categorization
            f.write(output)

    print('plot polygon and points')
    plotter.show()


if __name__ == '__main__':
    main()
