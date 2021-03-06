# import pi from math module
from math import pi


class AngleConversion:

    @staticmethod  # static method because it is not bound to the class
    def get_conversion_type() -> int:  # get conversion type from user, type hint: returns int
        conversion_type = None
        while conversion_type not in [1, 2]:  # while user input is anything else than 1 or 2
            try:
                conversion_type = int(input("Enter 1 or 2 to choose the type of conversion."
                                            + " Which type of angle conversion do you need?\n(1) rad to degree\n"
                                              "(2) degree to rad\n"))
            except ValueError:  # except value error for any input which is not int
                print("Please enter 1 or 2 to choose the type of conversion.")
        return conversion_type

    @staticmethod
    def get_angle_to_convert() -> float:  # get angle to convert from user,  returns float
        angle_to_convert = None
        while not isinstance(angle_to_convert, float):
            try:
                angle_to_convert = float(input("Enter the angle you want to convert "))
            except ValueError:  # except value error for not numerical input, error rises because of float()
                print("The angle has to be a numeral\nPlease enter a valid value")
        return angle_to_convert

    @staticmethod
    def convert_angle(conversion_type: int, angle_to_convert: float) -> float:
        converted_angle = None
        if conversion_type == 1:  # rad to degree
            converted_angle = round((360 / (2 * pi)) * angle_to_convert, 2)
            print(str(angle_to_convert) + " rad is equal to " + str(converted_angle) + " degree")
        elif conversion_type == 2:  # degree to rad
            converted_angle = round((angle_to_convert / 180) * pi, 2)
            print(str(angle_to_convert) + " degree is equal to " + str(converted_angle) + " rad")
        return converted_angle


# run = AngleConversion.convert_angle(AngleConversion.get_conversion_type(),
#                                    AngleConversion.get_angle_to_convert())

