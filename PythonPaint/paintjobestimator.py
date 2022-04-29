import math
# constants used within paint job estimator
LABOR_CHARGE = 62.25
WALL_SQUARE_FEET = 350
HOURS_PER_WALL = 6

do_estimate = True
while(do_estimate):

    while(True):
        try:
            inputted_square_feet = int(input("Please enter square feet of wall space: "))
            inputted_price_of_paint = float(input("Please enter price of paint per gallon: "))
            if(inputted_square_feet <= 0 or inputted_price_of_paint <= 0):
                print("Value must be positive. Please try a different value")
                continue
        except ValueError:
            print("The value you entered is invalid.  Only numerical values are valid.")
        else:
            break

    gallons_required = inputted_square_feet / WALL_SQUARE_FEET
    rounded_gallons = math.ceil(gallons_required)
    labor_hours = gallons_required * HOURS_PER_WALL
    paint_cost = inputted_price_of_paint * rounded_gallons
    labor_charges = LABOR_CHARGE * labor_hours
    total_cost = paint_cost + labor_charges

    print("Gallons of paint required: ", rounded_gallons)
    print("Hours of Labor Required: ", "{:.1f}".format(labor_hours))
    print("Cost of paint: ", "${:.2f}".format(paint_cost))
    print("Labor Charges: ", "${:.2f}".format(labor_charges))
    print("Total Cost: ", "${:.2f}".format(total_cost))

    another_estimate = input("\nWould you like to do another estimate? (y/n): ")
    if (another_estimate != "y"):
        do_estimate = False
