#import mysql.connector
import os


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    return

def numberOfRowsInDB():
    try:
        connection = mysql.connector.connect(host='mysql-server-1.mysql.database.azure.com',
                                             database='image-database',
                                             user='mysqladminu@mysql-server-1',
                                             password='STRONG_password@4534!')
        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT count(*) from 'image-table';"""

        cursor.execute(sql_fetch_blob_query)
        countRec = cursor.fetchall()
        print("CountRec:", countRec)
        connection.close()
        cursor.close()
        return countRec
    except:
        print("error connecting to database")
        return -1

def readBLOB(emp_id, photo, bioData):
    print("Reading BLOB data from python_employee table")
    try:
        connection = mysql.connector.connect(host='mysqld.mysql.database.azure.com',
                                             database='images',
                                             user='databasetier@mysqld',
                                             password='8864822055Yashika')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from python_employee where id = %s"""

        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        print(record)
        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            image = row[2]
            file = row[3]
            print("Storing employee image and bio-data on disk \n")
            write_file(image, photo)
            write_file(file, bioData)

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return
def getImageFromDB(i):
    try:
        connection = mysql.connector.connect(host='mysql-server-1.mysql.database.azure.com',
                                             database='image-database',
                                             user='mysqladminu@mysql-server-1',
                                             password='STRONG_password@4534!')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from image-table where index = %s"""

        cursor.execute(sql_fetch_blob_query, (i,))
        record = cursor.fetchall()
        '''
        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            image = row[2]
            file = row[3]
            print("Storing employee image and bio-data on disk \n")
            write_file(image, photo)
            write_file(file, bioData)
        '''
        photo_path = "downloads_db/"+record[2]
        write_file(record[1], photo_path)
        connection.close()
        cursor.close()
        return photo_path, record[2]
    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))
        return "e", "rror"

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def DBImgDelete(celebrityName):
    os.remove("downloads_db/"+str(celebrityName))

#readBLOB(1,r"C:\Users\yatin\OneDrive\Desktop\kapildev1.jpg",r"C:\Users\yatin\OneDrive\Desktop\runthecode1.txt")
