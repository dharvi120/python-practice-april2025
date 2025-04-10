# List Comprehension
squares = [x**2 for x in range(1, 11)]

# Map
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x*x, nums))

# Filter
evens = list(filter(lambda x: x % 2 == 0, range(1, 21)))

# Lambda sort
data = [(1, 2), (3, 1), (5, 0)]
sorted_data = sorted(data, key=lambda x: x[1])

# Bonus: Capitalize names
names = ['dharvi', 'shivam', 'ayushi']
upper_names = list(map(lambda name: name.upper(), names))

print(upper_names)
