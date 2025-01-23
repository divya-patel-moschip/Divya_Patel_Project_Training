"""
This is a program that demonstrate the use of python script with MySQL database server.
module : pip install mysql-connector-python
"""

import mysql.connector
from mysql.connector import Error
import logging

logger=logging.getLogger("sql_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('sql_log.log', 'w')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

console_handler=logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def insert_record(conn, user_name, email):
    """
    Inserting record inside the MySQL database.
    :param conn:
    :param user_name:
    :param email:
    :return:
    """
    if conn.is_connected():
        with conn.cursor() as cursor:
            cursor.execute(f"INSERT INTO users (name, email) VALUES ('{user_name}', '{email}');")
            conn.commit()
            logger.info(f"Record inserted successfully, Row ID : {cursor.lastrowid}")

def read_record_of_all_users(conn):
    """
    Fetching all the data from the database for 'users' table.
    :param conn:
    :return:
    """
    if conn.is_connected():
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name, email FROM users;")
            result = cursor.fetchall()
            for rows in result:
                print(rows)
    print()

def read_record_of_one_user(conn, user_name):
    """
    Fetching only records of the particular person from the 'users' table.
    :param conn:
    :param user_name:
    :return:
    """
    if conn.is_connected():
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT id, name, email FROM users WHERE name='{user_name}';")
            result = list(cursor.fetchone())
            print(result)
    print()
    return result[0]

def update_record_of_user(conn, user_name):
    """
    Updating record of already available data by fetching it from the database.
    :param conn:
    :param user_name:
    :return:
    """
    if conn.is_connected():
        id_no = read_record_of_one_user(conn, user_name)
        user_name = input("Enter the new user name : ")
        email = input("Enter the new email id : ")
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE users SET name='{user_name}', email='{email}' WHERE id={id_no};")
            conn.commit()
            logger.info(f"Record updated successfully, Row ID : {id_no}")

def delete_record(conn, user_name):
    """
    Deleting a record of particular user_name from the database by fetching it's id.
    :param conn:
    :param user_name:
    :return:
    """
    if conn.is_connected():
        id_no = read_record_of_one_user(conn, user_name)
        with conn.cursor() as cursor:
            cursor.execute(f"DELETE FROM users WHERE id={id_no};")
            conn.commit()
            logger.info(f"Record deleted successfully from database...")


if __name__ == "__main__":
    connection = mysql.connector.connect(
        host = 'localhost',
        user = "divya",
        password = "Soft@123",
        database = "dev_demo"
    )

    try:
        while True:
            print("Available operations for database:"
                  "\n1. Insert data"
                  "\n2. Update data"
                  "\n3. Read data"
                  "\n4. Delete data")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                logger.info(f"Insert operation is on going:")
                username = input("Enter the name: ")
                email_id = input("Enter the email id: ")
                insert_record(connection, username, email_id)
            elif choice == 2:
                logger.info(f"Update operation is on going:")
                username = input("Enter the name: ")
                update_record_of_user(connection, username)
            elif choice == 3:
                logger.info(f"Reading operation is on going: ")
                read_record_of_all_users(connection)
            elif choice == 4:
                logger.info(f"Deleting operation is on going: ")
                username = input("Enter the name: ")
                delete_record(connection, username)
            else:
                logger.info("Quiting from the program :")
                break

    except Error as e:
        logger.error(e.msg + " ====> Solve it now ASAP")
    finally:
        if connection.is_connected():
            connection.close()
            logger.info("MySQL connection is closed")