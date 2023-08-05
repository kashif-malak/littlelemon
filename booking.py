import pymysql

# Establish a connection to the database
connection = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    db='LittleLemon'
)

def get_max_quantity(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT MAX(Quantity) FROM BookingItems")
        result = cursor.fetchone()
        print(f"The maximum quantity in the BookingItems table is: {result[0]}")

def manage_booking(connection, booking_id, new_status):
    with connection.cursor() as cursor:
        sql = "UPDATE Bookings SET Status = %s WHERE BookingID = %s"
        cursor.execute(sql, (new_status, booking_id))
        connection.commit()

def update_booking(connection, booking_id, new_date):
    with connection.cursor() as cursor:
        sql = "UPDATE Bookings SET DeliveryDate = %s WHERE BookingID = %s"
        cursor.execute(sql, (new_date, booking_id))
        connection.commit()

def add_booking(connection, booking_id, booking_date, delivery_date, customer_id, status, booking_items):
    with connection.cursor() as cursor:
        sql = "INSERT INTO Bookings (BookingID, BookingDate, DeliveryDate, CustomerID, Status) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (booking_id, booking_date, delivery_date, customer_id, status))
        for item in booking_items:
            sql = "INSERT INTO BookingItems (BookingID, ItemID, Quantity) VALUES (%s, %s, %s)"
            cursor.execute(sql, (booking_id, item['item_id'], item['quantity']))
        connection.commit()

def cancel_booking(connection, booking_id):
    manage_booking(connection, booking_id, 'Cancelled')
