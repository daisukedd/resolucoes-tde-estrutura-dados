matrix = [
    [0, 15, 20, 5, 10],
    [15, 0, 10, 12, 28],
    [20, 10, 0, 8, 16],
    [5, 12, 8, 0, 14],
    [10, 28, 16, 14, 0]
]

total_distance = 0
route = []
n = len(matrix)

print(f"The matrix has {n} rows and {n} columns (0 to {n-1}).")
print("Enter up to 6 coordinates [row,column] for the route:")

for i in range(6):
    entry = input(f"Coordinate {i+1} [row,column] or ENTER to stop: ")
    if not entry:
        break
    
    try:
        row, col = map(int, entry.split(","))
        if 0 <= row < n and 0 <= col < n:
            distance = matrix[row][col]
            print(f"Distance between ({row},{col}) = {distance} km")
            total_distance += distance
            route.append((row, col, distance))
        else:
            print(f"Invalid coordinate. Use numbers between 0 and {n-1}.")
    except:
        print("Invalid input, use the format row,column")

print("\nComplete route:")
for row, col, distance in route:
    print(f"({row},{col}) = {distance} km")

print(f"Total distance: {total_distance} km")
