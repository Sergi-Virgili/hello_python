users = [
    {"name": "Alice", "age": 25, "phone": "628546595"},
    {"name": "Bob", "age": 30, "phone": "628546596"},
    {"name": "Charlie", "age": 35, "phone": "628546597"},
]

# pide el nombre, la edad y el telefono lo guarda en la lista de usuarios
name = input("Name: ")
age = int(input("Age: "))
phone = input("Phone: ")

users.append({"name": name, "age": age, "phone": phone})

# Print the header
print(" | ".join(users[0].keys()))

# Print the users
for user in users:
    print(f"{user['name']} | {user['age']} | {user['phone']}")
