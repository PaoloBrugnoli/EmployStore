import mysql.connector
from mysql.connector import errorcode
from capgemini.store.resourses.sql import *
from capgemini.store.utility.replace import MakeQuery


# TABLE empDetails
class DaoEmpDetails:
    def __init__(self, host, user, passwd, database):  # Here, name is the library name
        self.config = {
            "user": user,
            "password": passwd,
            "host": host,
            "database": database,
            "raise_on_warnings": True,
        }

    # Insert Data Function
    def insert_data(self, id_emp, name, dept):
        b_response = True
        s_msg = ""
        try:
            cnx = mysql.connector.connect(**self.config)
            s_config = self.config["host"] + " - " + self.config["database"]
            print(f"OPENED CONNECTION TO DB : {s_config}")
            # Make dynamic query
            d_date = {
                "{id}": id_emp,
                "{name}": name,
                "{dept}": dept
            }

            mq = MakeQuery(insert_to_emp, d_date)
            sql_query = mq.get_sql()
            print(f"Query : {sql_query}")

            cursor = cnx.cursor()
            cursor.execute(sql_query)
            cnx.commit()

            s_msg = "Record inserted successfully into Laptop table"
            print(cursor.rowcount, s_msg)
            cursor.close()

        except mysql.connector.Error as error:
            b_response=False
            s_msg = "Failed to insert record into Laptop table : {}".format(error)
            print(s_msg)

        finally:
            if cnx.is_connected():
                cnx.close()
                print("MySQL is closed")

        return b_response, s_msg

    # Update Data Function
    def update_data(self, id_emp, name, dept):
        b_response = True
        s_msg = ""
        try:
            cnx = mysql.connector.connect(**self.config)
            s_config = self.config["host"] + " - " + self.config["database"]
            print(f"OPENED CONNECTION TO DB : {s_config}")
            # Make dynamic query
            d_date = {
                "{id}": id_emp,
                "{name}": name,
                "{dept}": dept
            }

            mq = MakeQuery(update_to_emp, d_date)
            sql_query = mq.get_sql()
            print(f"Query : {sql_query}")

            cursor = cnx.cursor()
            cursor.execute(sql_query)
            cnx.commit()

            s_msg = "Record updated successfully into Laptop table"
            print(cursor.rowcount, s_msg)
            cursor.close()

        except mysql.connector.Error as error:
            b_response = False
            s_msg = "Failed to update record into Laptop table : {}".format(error)
            print(s_msg)

        finally:
            if cnx.is_connected():
                cnx.close()
                print("MySQL is closed")

        return b_response, s_msg

    # get Data Function
    def get_data(self, id_emp):
        d_response = {}
        b_response = True
        s_msg = ""
        try:
            cnx = mysql.connector.connect(**self.config)
            s_config = self.config["host"] + " - " + self.config["database"]
            print(f"OPENED CONNECTION TO DB : {s_config}")
            # Make dynamic query
            d_date = {
                "{id}": id_emp
            }

            mq = MakeQuery(select_to_emp, d_date)
            sql_query = mq.get_sql()
            print(f"Query : {sql_query}")

            cursor = cnx.cursor()
            cursor.execute(sql_query)

            # get all records
            records = cursor.fetchall()
            print("Total number of rows in tables :", cursor.rowcount)
            print("\nPrinting each row")
            for row in records:
                print(f"[id : {row[1]}] [Name : {row[1] } ; Dept : {row[2]}]")
                s_info = row[1] + ";" + row[2]
                d_response.update({row[0]: s_info})

            s_msg = "Record successfully read from  Laptop table"
            print(cursor.rowcount, s_msg)
            cursor.close()

        except mysql.connector.Error as error:
            b_response = False
            s_msg = "Error reading data from MySQL table : {}".format(error)
            print(s_msg)

        finally:
            if cnx.is_connected():
                cnx.close()
                print("MySQL is closed")

        return b_response, s_msg, d_response

    # Delete Data Function
    def delete_data(self, id_emp):
        b_response = True
        s_msg = ""
        try:
            cnx = mysql.connector.connect(**self.config)
            s_config = self.config["host"] + " - " + self.config["database"]
            print(f"OPENED CONNECTION TO DB : {s_config}")
            # Make dynamic query
            d_date = {
                "{id}": id_emp
            }

            mq = MakeQuery(delete_to_emp, d_date)
            sql_query = mq.get_sql()
            print(f"Query : {sql_query}")

            cursor = cnx.cursor()
            cursor.execute(sql_query)

            cnx.commit()

            s_msg = "Record deleted successfully into Laptop table"
            print(cursor.rowcount, s_msg)
            cursor.close()

        except mysql.connector.Error as error:
            b_response = False
            s_msg = "Failed to delete record into Laptop table : {}".format(error)
            print(s_msg)

        finally:
            if cnx.is_connected():
                cnx.close()
                print("MySQL is closed")

        return b_response, s_msg

    # Show Data Function
    def show_data(self):
        d_response = {}
        b_response = True
        s_msg = ""
        try:
            cnx = mysql.connector.connect(**self.config)
            s_config = self.config["host"] + " - " + self.config["database"]
            print(f"OPENED CONNECTION TO DB : {s_config}")
            # Make dynamic query

            sql_query = select_all_to_emp
            print(f"Query : {sql_query}")

            cursor = cnx.cursor()
            cursor.execute(sql_query)

            # get all records
            records = cursor.fetchall()
            print("Total number of rows in tables :", cursor.rowcount)
            print("\nPrinting each row")
            for row in records:
                print(f"[id : {row[1]}] [Name : {row[1] } ; Dept : {row[2]}]")
                s_info = row[1] + ";" + row[2]
                d_response.update({row[0]: s_info})

            s_msg = "Record successfully read from  Laptop table"
            print(cursor.rowcount, s_msg)
            cursor.close()

        except mysql.connector.Error as error:
            b_response = False
            s_msg = "Error reading data from MySQL table : {}".format(error)
            print(s_msg)

        finally:
            if cnx.is_connected():
                cnx.close()
                print("MySQL is closed")

        return b_response, s_msg, d_response


