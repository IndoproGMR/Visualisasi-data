import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def connect_to_mysql():
    try:
        # Konfigurasi koneksi ke MySQL
        connection = mysql.connector.connect(
            host=os.getenv('host'),
            user=os.getenv('user'),
            password=os.getenv('password'),
            database=os.getenv('database'),
        )

        if connection.is_connected():
            # print("Berhasil terhubung ke database MySQL")
            return connection
        else:
            # print("Gagal terhubung ke database MySQL")
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def close_mysql_connection(connection):
    if connection:
        connection.close()
        # print("Koneksi ke MySQL ditutup")


# Contoh penggunaan
# if __name__ == "__main__":
    # db_connection = connect_to_mysql()

    # Lakukan operasi-operasi database di sini

    # Tutup koneksi setelah selesai
    # close_mysql_connection(db_connection)
