# You have a list of objects with dimensions, write code to find a box that would fit the largest object

class dimensional_object():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    def __repr__(self):
        return f"dimensional_object(length={self.x}, width={self.y}, height={self.z})"

dimmensional_objects = [
    dimensional_object(1, 2, 3),
    dimensional_object(4, 5, 6),
    dimensional_object(10, 11, 12),
    dimensional_object(1, 14, 3),
    dimensional_object(4, 4, 14),
    dimensional_object(1, 1, 1),
]


def find_largest_object(objects):
    """Find the box that would fit the largest object"""
    largest_object = max(objects, key=lambda obj: obj.volume())
    return largest_object.volume(), largest_object.x, largest_object.y, largest_object.z


def main():
    #
    # Find the box that would fit the largest object
    largest_volume, length, width, height = find_largest_object(dimmensional_objects)
    print(f"The largest object has a volume of {largest_volume} and dimensions: length={length}, width={width}, height={height}")




if __name__ == "__main__":
        main()