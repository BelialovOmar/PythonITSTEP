# #!C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe

# import os
# import cgi
# import html
# import cgitb; cgitb.enable()
# import mysql.connector

# # Функція для аналізу рядка запиту
# def parse_query_string(query):
#     params = {}
#     if query:
#         pairs = query.split('&')
#         for pair in pairs:
#             key, value = pair.split('=')
#             params[key] = value
#     return params

# def fetch_databases():
#     db_ini = {
#         'host': 'localhost',
#         'port': 3306,
#         'user': 'py202_user',
#         'password': 'pass_202',
#         'database': 'py202',
#         'charset': 'utf8mb4',
#         'use_unicode': True,
#         'collation': 'utf8mb4_unicode_ci'
#     }
#     db_connection = mysql.connector.connect(**db_ini)
#     cursor = db_connection.cursor()
#     cursor.execute("SHOW DATABASES")
#     databases = cursor.fetchall()
#     cursor.close()
#     db_connection.close()
#     return databases

# def generate_html_table(data):
#     html_content = "<table border='1'><tr><th>Database Name</th></tr>"
#     for row in data:
#         html_content += f"<tr><td>{html.escape(row[0])}</td></tr>"
#     html_content += "</table>"
#     return html_content

# print("Content-Type: text/html; charset=utf-8")
# print()

# print("<html><body>")
# print("<h1>Список баз даних</h1>")

# databases = fetch_databases()
# print(generate_html_table(databases))

# print("<h2>Змінні оточення:</h2>")
# env_vars = ['REQUEST_URI', 'QUERY_STRING', 'REQUEST_METHOD', 'REMOTE_ADDR', 'REQUEST_SCHEME']
# env_values = {var: os.environ.get(var, '') for var in env_vars}
# for var, value in env_values.items():
#     print(f"<p>{var}: {html.escape(value)}</p>")

# print("<h2>Розібраний QUERY_STRING:</h2>")
# query_string = os.environ.get('QUERY_STRING', '')
# parsed_query = parse_query_string(query_string)
# print("<ul>")
# for key, value in parsed_query.items():
#     print(f"<li>{html.escape(key)}: {html.escape(value)}</li>")
# print("</ul>")

# print("</body></html>")

#!C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe

import os

envs = f"<ul>{''.join([f'<li>{k} = {v}</li>' for k, v in os.environ.items()])}</ul>"

print("Content-Type: text/html; charset=cp1251")
print("Connection: close")
print()   # порожній рядок - кінець заголовків
with open( 'home.html' ) as file :
    print( file.read() )
