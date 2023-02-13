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



import sys

def convert_to_ml(amount, unit):
    if unit == 'pint':
        return amount * 473.176
    elif unit == 'quart':
        return amount * 946.353
    elif unit == 'cup':
        return amount * 236.588
    elif unit == 'ml':
        return amount
    elif unit == 'dl':
        return amount * 100
    elif unit == 'L':
        return amount * 1000
    else:
        return 'Invalid unit'

def convert(amount, from_unit, to_unit):
    ml_amount = convert_to_ml(amount, from_unit)
    if to_unit == 'pint':
        return ml_amount / 473.176
    elif to_unit == 'quart':
        return ml_amount / 946.353
    elif to_unit == 'cup':
        return ml_amount / 236.588
    elif to_unit == 'ml':
        return ml_amount
    elif to_unit == 'dl':
        return ml_amount / 100
    elif to_unit == 'L':
        return ml_amount / 1000
    else:
        return 'Invalid unit'

if __name__ == '__main__':
    amount = float(sys.argv[1])
    from_unit = sys.argv[3]
    to_unit = sys.argv[5]

    result = convert(amount, from_unit, to_unit)
    print(f'{amount} {from_unit} is equal to {result} {to_unit}')