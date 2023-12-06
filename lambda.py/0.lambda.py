# A lambda function that adds two numbers
add = lambda x, y: x + y

result = add(3, 5)
print(result) 


#Sorting a list of tuples based on the second element using lambda
points = [(1, 2), (3, 1), (5, 4), (2, 0)]
points_sorted = sorted(points, key=lambda x: x[1])

print(points_sorted)
