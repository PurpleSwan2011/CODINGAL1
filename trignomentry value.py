import math

# Function to calculate trigonometric values
def calculate_trigonometric_values(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    
    sine_value = math.sin(angle_radians)
    cosine_value = math.cos(angle_radians)
    tangent_value = math.tan(angle_radians)
    
    return sine_value, cosine_value, tangent_value

# Example usage
angle = 45  # You can change this angle to any value you want
sine, cosine, tangent = calculate_trigonometric_values(angle)

print(f"Trigonometric values for {angle} degrees:")
print(f"Sine: {sine}")
print(f"Cosine: {cosine}")
print(f"Tangent: {tangent}")