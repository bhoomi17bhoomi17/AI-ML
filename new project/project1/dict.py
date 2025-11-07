# Creating dictionary
person = {
"name": "Alice",
"age": 25,
"city": "New York"
}
print(person) # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Accessing values
print(person["name"]) # Output: Alice
print(person["age"]) # Output: 25
# Adding/Modifying entries
person["email"] = "alice@email.com"
person["age"] = 26
print(person)
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@email.com'}
# Removing entries
del person["email"]
print(person) # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}
# Check if key exists
if "name" in person:
            print("Name exists!") # Output: Name exists!
# Loop through dictionary
for key in person:
             print(f"{key}: {person[key]}")
# Output:
# name: Alice
# age: 26
# city: New York
# Get keys and values
print(person.keys()) # Output: dict_keys(['name', 'age', 'city'])
print(person.values()) # Output: dict_values(['Alice', 26, 'New York'])
print(person["name"])
print(person["age"])
