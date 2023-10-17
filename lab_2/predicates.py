import abc
import math

from lab_2.utils import calculate_distance


class Figure(abc.ABC):
    def __init__(self, vertices: list):
        self.vertices = vertices

    @property
    @abc.abstractmethod
    def is_equal_sides(self) -> bool:
        pass

    @property
    @abc.abstractmethod
    def has_right_angle(self) -> bool:
        pass


class Triangle(Figure):
    @property
    def is_equal_sides(self):
        side1 = calculate_distance(self.vertices[0], self.vertices[1])
        side2 = calculate_distance(self.vertices[1], self.vertices[2])
        side3 = calculate_distance(self.vertices[2], self.vertices[0])
        return side1 == side2 == side3

    @property
    def has_right_angle(self):
        side_lengths = [
            calculate_distance(self.vertices[0], self.vertices[1]),
            calculate_distance(self.vertices[1], self.vertices[2]),
            calculate_distance(self.vertices[2], self.vertices[0]),
        ]
        side_lengths.sort()
        return math.isclose(
            side_lengths[0] ** 2 + side_lengths[1] ** 2, side_lengths[2] ** 2
        )


class Square(Triangle):
    @property
    def is_equal_sides(self):
        side_lengths = [
            calculate_distance(self.vertices[0], self.vertices[1]),
            calculate_distance(self.vertices[1], self.vertices[2]),
            calculate_distance(self.vertices[2], self.vertices[3]),
            calculate_distance(self.vertices[3], self.vertices[0]),
        ]
        return all(side == side_lengths[0] for side in side_lengths)

    @property
    def has_right_angle(self):
        side_lengths = [
            calculate_distance(self.vertices[0], self.vertices[1]),
            calculate_distance(self.vertices[1], self.vertices[2]),
            calculate_distance(self.vertices[2], self.vertices[3]),
            calculate_distance(self.vertices[3], self.vertices[0]),
        ]
        diagonals = [
            calculate_distance(self.vertices[0], self.vertices[2]),
            calculate_distance(self.vertices[1], self.vertices[3]),
        ]
        diagonals.sort()
        return math.isclose(
            side_lengths[0] ** 2 + side_lengths[2] ** 2,
            diagonals[0] ** 2 + diagonals[1] ** 2,
        )


class Circle(Figure):
    @property
    def is_equal_sides(self):
        print("Circle always has equal sides.")
        return True

    @property
    def has_right_angle(self):
        print("A circle can't have a right angle.")
        return False


class Rectangle(Square):
    @property
    def is_equal_sides(self):
        side_lengths = [
            calculate_distance(self.vertices[0], self.vertices[1]),
            calculate_distance(self.vertices[1], self.vertices[2]),
            calculate_distance(self.vertices[2], self.vertices[3]),
            calculate_distance(self.vertices[3], self.vertices[0]),
        ]
        return all(side == side_lengths[0] for side in side_lengths)

    @property
    def has_right_angle(self):
        side_lengths = [
            calculate_distance(self.vertices[0], self.vertices[1]),
            calculate_distance(self.vertices[1], self.vertices[2]),
            calculate_distance(self.vertices[2], self.vertices[3]),
            calculate_distance(self.vertices[3], self.vertices[0]),
        ]
        diagonals = [
            calculate_distance(self.vertices[0], self.vertices[2]),
            calculate_distance(self.vertices[1], self.vertices[3]),
        ]
        diagonals.sort()
        return math.isclose(
            side_lengths[0] ** 2 + side_lengths[2] ** 2,
            diagonals[0] ** 2 + diagonals[1] ** 2,
        )


# Example usage
triangle = Triangle([(0, 0), (0, 3), (4, 0)])
square = Square([(0, 0), (0, 2), (2, 2), (2, 0)])
circle = Circle([(0, 0), 5])
rectangle = Rectangle([(0, 0), (0, 3), (4, 0), (4, 3)])


if __name__ == "__main__":
    print(triangle.is_equal_sides)  # False
    print(triangle.has_right_angle)  # True
    print(square.is_equal_sides)  # True
    print(square.has_right_angle)  # True
    print(circle.is_equal_sides)  # Circle always has equal sides.
    print(circle.has_right_angle)  # A circle can't have a right angle.
    print(rectangle.is_equal_sides)  # True
    print(rectangle.has_right_angle)  # True
