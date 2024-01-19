#!C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe

import os
import cgi
import html
import cgitb; cgitb.enable()
import mysql.connector

# Функція для підключення до бази даних і виконання запиту
def fetch_databases():
    db_ini = {
        'host': 'localhost',
        'port': 3306,
        'user': 'py202_user',
        'password': 'pass_202',
        'database': 'py202',
        'charset': 'utf8mb4',
        'use_unicode': True,
        'collation': 'utf8mb4_unicode_ci'
    }
    db_connection = mysql.connector.connect(**db_ini)
    cursor = db_connection.cursor()
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    cursor.close()
    db_connection.close()
    return databases

# Генерація HTML-таблиці з результатами
def generate_html_table(data):
    html_content = "<table border='1'><tr><th>Database Name</th></tr>"
    for row in data:
        html_content += f"<tr><td>{html.escape(row[0])}</td></tr>"
    html_content += "</table>"
    return html_content

# Основний код
print("Content-Type: text/html; charset=utf-8")
print()

print("<html><body>")
print("<h1>Список баз даних</h1>")

# Викликаємо функцію fetch_databases і виводимо результат у таблиці
databases = fetch_databases()
print(generate_html_table(databases))

print("</body></html>")
