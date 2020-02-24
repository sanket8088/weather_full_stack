from django.core.management.base import BaseCommand
import mysql.connector

from django.utils import timezone

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        host = input("Enter host address")
        user = input("Enter user name")
        password = input("Enter password")
        db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
        )
        print(db)

        mycursor = db.cursor()
        # mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
        # mycursor.execute("CREATE DATABASE mydatabase")
        mycursor.execute("CREATE TABLE mydatabase.customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


        


