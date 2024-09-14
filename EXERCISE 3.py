import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="POOH",
    database="airport_database",
    collation="utf8mb4_general_ci"
)

cursor = conn.cursor()

if conn.is_connected():
    print("Connected to MariaDB")

def main():
    airports = {}

    while True:
        print("Choose an option:")
        print("1. Enter a new airport")
        print("2. Fetch the information of an existing airport")
        print("3. Quit")

        choice = input("Enter your choice (1 or 2 or 3):")
        if choice == "1":
            icao = input("Enter the ICAO code of the airport:").upper()
            name = input("Enter the name of the airport:")

            insert_query = "INSERT INTO airport (ICAO_CODE, AIRPORT_NAME) VALUES (%s, %s)"
            values = (icao, name)

            cursor.execute(insert_query, values)
            conn.commit()
            print(f"Airport {name} with ICAO code {icao} successfully added.")

        elif choice == "2":
            icao_Input = input("Enter the ICAO code of the airport to fetch:").upper()
            select_query = "SELECT * FROM airport where ICAO_CODE = %s "
            cursor.execute(select_query, (icao_Input,))

            result = cursor.fetchall()

            if result:
                first_row = result[0]
                airport_name = first_row[2]
                print(f"The airport name for ICAO code {icao_Input} is: {airport_name}")
            else:
                print(f"No airport found with ICAO code {icao_Input}.")
        elif choice == "3":
            print("Exiting the program.")
            cursor.close()
            conn.close()
            break
        else:
            print("Invalid choice. Please enter 1,2, or 3.")

main()
