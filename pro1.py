import math

def calculate_circle_properties(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        if radius < 0:
            print("Radius cannot be negative. Please enter a positive value.")
        else:
            area, perimeter = calculate_circle_properties(radius)
            print(f"Area of the circle: {area:.2f}")
            print(f"Perimeter (Circumference) of the circle: {perimeter:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numerical value for the radius.")

if __name__ == "__main__":
    main()
