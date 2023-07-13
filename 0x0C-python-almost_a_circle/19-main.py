#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(4, 5, 6, 2, 44)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()
    
    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    
    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))
    print("---")
    print("---")

    s1 = Square(2, 1, 4, 44)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()
    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

    sq1 = Square(2, 1, 2, 42)
    sq2 = Square(4, 2, 1, 24)
    Square.save_to_file([sq1, sq2])
    with open("Square.json", 'r') as rad:
        print(len(rad.read()))
    r3 = Rectangle(4, 5, 6, 2, 44)
    Rectangle.save_to_file([r3])
    with open("Rectangle.json", 'r') as rad:
        print(len(rad.read()))
