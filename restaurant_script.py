#Initial values of the variables

orders = {}
plate_number = 0

# Taking orders from the user
table_number = input("Table number: ")
a_plate = input("Type 1 to order a plate or 0 to procced: ")
while a_plate != "0":
    if a_plate == '1':
        plate_number = plate_number + 1
        a_plate = '0'
        main_course = input("Main course: ")
        garnishes = input("Garnishes: ")
        orders [plate_number] = [main_course, garnishes]
    a_plate = input("Type 1 to order a plate or 0 to procced: ")

print(f"Orders for table {table_number}:")

for plate_number, order in orders.items():
    print(f"Plate {plate_number}: {order}")

print("Orders have been taken successfully.")
# Displaying the orders in a structured format
