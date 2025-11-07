#Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]
print(fruits) # Output: ['apple', 'banana', 'cherry']
# Accessing elements (index starts at 0)
print(fruits[0]) # Output: apple
print(fruits[1]) # Output: banana
print(fruits[-1]) # Output: cherry (last item)
# Modifying lists
fruits[1] = "blueberry"
print(fruits) # Output: ['apple', 'blueberry', 'cherry']
# List length
print(len(fruits)) # Output: 3
# Adding elements
fruits.append("date") # Add to end
print(fruits) # Output: ['apple', 'blueberry', 'cherry', 'date']
fruits.insert(1, "banana") # Insert at index
print(fruits) # Output: ['apple', 'banana', 'blueberry', 'cherry', 'date']
# Removing elements
fruits.remove("banana") # Remove by value
print(fruits) # Output: ['apple', 'blueberry', 'cherry', 'date']
last = fruits.pop() # Remove and return last item
print(last) # Output: date
print(fruits) # Output: ['apple', 'blueberry', 'cherry']

# Loop through list
for fruit in fruits:
     print(fruit)
# Output:
# apple
# blueberry
# cherry
# Check if item exists
if "apple" in fruits:
  print("Apple is in the list") # Output: Apple is in the list
numbers = [1, 2, 3, 4, 5]
print(numbers[2:4]) # Output: [2, 3, 4]
print(numbers[:3]) # Output: [1, 2, 3]
print(numbers[2:]) # Output: [3, 4, 5]