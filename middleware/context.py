
import os

# This is a bad place for this import
import pymysql

def get_db_info():
    """
    This is crappy code.

    :return: A dictionary with connect info for MySQL
    """
    # db_host = os.environ.get("DBHOST", None)
    # db_user = os.environ.get("DBUSER", None)
    # db_password = os.environ.get("DBPASSWORD", None)
    db_host = "database-1.cxutdoariico.ap-northeast-1.rds.amazonaws.com"
    db_user = "admin"
    db_password = "12345678"

    print(db_host)

    if db_host is not None:
        db_info = {
            "host": db_host,
            "user": db_user,
            "password": db_password,
            "cursorclass": pymysql.cursors.DictCursor
        }

    else:
        db_info = {
            "host": "localhost",
            "user": "root",
            "password": "118871356",
            "cursorclass": pymysql.cursors.DictCursor
        }


    return db_info
