import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates) # 3 dimensions if [1,2,3]

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    # Overwrites Python's default "print" function
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    # Overwrites Python's default == function
    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return new_coordinates        

    def times_scalar(self, c):
        new_coordinates = [c * x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        sq_coordinates = [math.pow(x, 2) for x in self.coordinates]
        sum_of_sq = sum(sq_coordinates)
        sqrt_of_sum = math.sqrt(sum_of_sq)
        return sqrt_of_sum

    def normalize(self):        
        magnitude = self.magnitude()
        unit_vector = [(1/magnitude)*x for x in self.coordinates]
        return unit_vector

