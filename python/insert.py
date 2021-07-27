import mysql.connector

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(emp_id, name, photo):
    print("Inserting BLOB into image-table table")
    try:
        connection = mysql.connector.connect(host='mysql-server-1.mysql.database.azure.com',
                                             database='image-database',
                                             user='mysqladminu@mysql-server-1',
                                             password='STRONG_password@4534!')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO `image-table` (`index`, `name`, `photo`) VALUES (%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)
        #file = convertToBinaryData(biodataFile)

        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into image-table table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(1, "Kapil Dev","/home/linux-vm/Documents/Internship 2021/Company-Project/Backend-Codes/google drive jo youtube video mai thi/Photograph/KapilDev_1.jpg")
insertBLOB(2, "Priyanka Chopra","/home/linux-vm/Documents/Internship 2021/Company-Project/Backend-Codes/google drive jo youtube video mai thi/Photograph/PriyankaChopra.jpg")
insertBLOB(3, "Kamal Hasan","/home/linux-vm/Documents/Internship 2021/Company-Project/Backend-Codes/google drive jo youtube video mai thi/Photograph/KamalHasan.jpg")
insertBLOB(4, "Sachin Tendulkar","/home/linux-vm/Documents/Internship 2021/Company-Project/Backend-Codes/google drive jo youtube video mai thi/Photograph/SachinTendulkar.jpg")
insertBLOB(5, "Aishwarya Rai","/home/linux-vm/Documents/Internship 2021/Company-Project/Backend-Codes/google drive jo youtube video mai thi/Photograph/AishwaryaRai.jpg")
