#!C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe

import os
import cgi
import html
import cgitb; cgitb.enable()

def parse_query_string(query):
    params = {}
    if query:
        pairs = query.split('&')
        for pair in pairs:
            key, value = pair.split('=')
            params[key] = value
    return params


env_vars = ['REQUEST_URI', 'QUERY_STRING', 'REQUEST_METHOD', 'REMOTE_ADDR', 'REQUEST_SCHEME']
env_values = {var: os.environ.get(var, '') for var in env_vars}

query_string = os.environ.get('QUERY_STRING', '')
parsed_query = parse_query_string(query_string)

print("Content-Type: text/html; charset=utf-8")
print()
print("<html><body>")
print("<h2>Змінні оточення:</h2>")
for var, value in env_values.items():
    print(f"<p>{var}: {html.escape(value)}</p>")

print("<h2>Розібраний QUERY_STRING:</h2>")
print("<ul>")
for key, value in parsed_query.items():
    print(f"<li>{html.escape(key)}: {html.escape(value)}</li>")
print("</ul>")
print("</body></html>")