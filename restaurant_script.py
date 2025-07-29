#Initial values of the variables

orders_plate = {}
orders_drink = {}
plate_number = 0
drink_number = 0

# Taking orders from the user

# Plates
table_number = input("Table number: ")
a_plate = input("Type 1 to order a plate or 0 to procced: ")
while a_plate != "0":
    if a_plate == '1':
        plate_number = plate_number + 1
        a_plate = '0'
        main_course = input("Main course: ")
        garnishes_plate = input("Garnishes: ")
        orders_plate [plate_number] = [main_course, garnishes_plate]
    a_plate = input("Type 1 to order a plate or 0 to procced: ")

# Drinks
a_drink = input("Type 1 to order a drink or 0 to procced: ")
while a_drink != "0":
    if a_drink == '1':
        drink_number = drink_number + 1
        a_drink = '0'
        drink = input("Drink: ")
        garnishes_drink = input("Garnishes: ")
        orders_drink [drink_number] = [drink, garnishes_drink]
    a_drink = input("Type 1 to order a drink or 0 to procced: ")

# Displaying the orders
print("\n")

print(f"Orders for table {table_number}:")

print()
for plate_number, order in orders_plate.items():
    print(f"Plate {plate_number}: {order}")

for drink_number, order in orders_drink.items():
    print(f"Drink {drink_number}: {order}")

print()

print("Orders have been taken successfully.")