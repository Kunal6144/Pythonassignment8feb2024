import random

def approximate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        # Generate random points inside the square [-1, 1] x [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if the point is inside the circle (unit circle with radius 1)
        if x**2 + y**2 < 1:
            points_inside_circle += 1

    # Calculate the approximation of pi using the formula: π ≈ 4 * (number of points inside circle / total number of points)
    pi_approximation = 4 * points_inside_circle / num_points
    return pi_approximation

if __name__ == "__main__":
    num_points = int(input("Enter the number of random points to generate: "))
    approximation = approximate_pi(num_points)
    print(f"Approximation of pi using {num_points} random points: {approximation}")
