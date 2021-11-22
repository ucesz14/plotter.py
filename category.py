class Geometry:
    def __init__(self, name):
        self.name = name

    def get_name(self):

        return self.name


class Point(Geometry):

    def __init__(self, name, x, y):
        super().__init__(name)
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


class Line(Geometry):
    def __init__(self, name, point_1, point_2):
        super().__init__(name)
        self.__point_1 = point_1
        self.__point_2 = point_2


class Polygon:
    def __init__(self):
        pass

    def pip(self, xs, ys, x, y):
        # xs is the list of the x and ys is the list of y of all polygon points

        x_min = min(xs)
        x_max = max(xs)
        y_min = min(ys)
        y_max = max(ys)
        # get the edge information for MBR

        is_in = False  # set the in initial situation which is false, which means outside

        if x_min <= x <= x_max and y_max >= y >= y_min:  # MBR method finished

            for i in range(len(xs)):
                if i == 0:
                    j = len(xs) - 1
                else:
                    j = i - 1
                # here i and j is two point close to each other on polygon, to create a line information

                if ys[i] == ys[j]:
                    if ys[i] == y and abs(xs[i] - x) + abs(xs[j] - x) == abs(xs[i] - xs[j]):
                        kind = 'boundary'
                        break
                # firstly consider the situation of function like y = n(constant), which will cause an error in the
                # following calculation, as (ys[j] - ys[i]) is 0. A number is /0.

                else:
                    if ((ys[i] > y) != (ys[j] > y)) and (x == (xs[j] - xs[i]) * (y - ys[i]) / (ys[j] - ys[i]) + xs[i]):
                        kind = 'boundary'
                        break
                    #  here means the point is on the line, so it should be boundary

                    elif ((ys[i] > y) != (ys[j] > y)) and (
                            x < (xs[j] - xs[i]) * (y - ys[i]) / (ys[j] - ys[i]) + xs[i]):

                        is_in = not is_in
                    # which means the ray from point get across a line of the polygon, so is_in change once

                # the method use the thinking of similar triangles, which is introduced in a blog,
                # citation: https://www.jianshu.com/p/39c63ab0a219

                if is_in:
                    kind = 'inside'
                else:
                    kind = 'outside'
                # Odd number is true so inside, even number is false so outside, RCA finished

        else:

            kind = 'outside'

        return kind


class Categorize:
    def __init__(self):
        pass

    def csv_r(self, file_name):
        num = []
        x = []
        y = []

        with open(file_name) as f:
            rows = f.readlines()[1:]  # start reading the data from second row

        try:
            for row in rows:
                num_t, x_t, y_t = row.split(',')

                num.append(float(num_t))

                x.append(float(x_t))

                y.append(float(y_t.strip()))  # y_t has '\n' so it need to use strip

        except ValueError:  # check the format of file and then give out a warning of error
            print('WARNING: The format of data have some problems. Please check the data file.')

        return x, y, num
