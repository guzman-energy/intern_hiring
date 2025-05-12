# You have a list of objects with dimensions, write code to find a box that would fit the largest object

class DimensionalObject():
    """A class to represent a 3D object with dimensions."""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        """Calculate the volume of the object."""
        return self.x * self.y * self.z

    def __repr__(self):
        return f"dimensional_object(length={self.x}, width={self.y}, height={self.z})"

dimmensional_objects = [
    DimensionalObject(1, 2, 3),
    DimensionalObject(4, 5, 6),
    DimensionalObject(10, 11, 12),
    DimensionalObject(1, 14, 3),
    DimensionalObject(4, 4, 14),
    DimensionalObject(1, 1, 1),
]


def main():
    # TODO
    # What dimensions would a box need to be to fit the all the objects?








if __name__ == "__main__":
        main()
