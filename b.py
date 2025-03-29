
def calculate_fare(distance):
    base_fare = 10  
    additional_fare_per_km = 2  
    
    if distance <= 5:
        return base_fare
    else:
        additional_distance = distance - 5
        total_fare = base_fare + (additional_distance * additional_fare_per_km)
        return total_fare

def main():
    try:
        distance = float(input("Enter the distance traveled (in km): "))
        if distance < 0:
            print("Distance cannot be negative. Please enter a valid distance.")
        else:
            fare = calculate_fare(distance)
            print(f"The bus fare for {distance} km is ₹{fare:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numerical value for distance.")

if __name__ == "__main__":
    main()
