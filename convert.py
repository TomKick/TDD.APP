import sys

def convert_to_mm(inches):
    return inches * 25.4

def convert_to_cm(inches):
    return inches * 2.54

def convert_to_m(inches):
    return inches / 39.37

if __name__ == '__main__':
    inches = float(sys.argv[1])
    unit = sys.argv[2]

    if unit == '-mm':
        result = convert_to_mm(inches)
        print(f"{result:.2f} mm")
    elif unit == '-cm':
        result = convert_to_cm(inches)
        print(f"{result:.2f} cm")
    elif unit == '-m':
        result = convert_to_m(inches)
        print(f"{result:.6f} m")
    elif unit == '-t':
        print("Running tests:")
        print("3 inches to mm:", convert_to_mm(3))
        print("3 inches to cm:", convert_to_cm(3))
        print("3 inches to m:", convert_to_m(3))
    else:
        print("Invalid unit argument. Choose one of [-mm, -cm, -m, -t]")