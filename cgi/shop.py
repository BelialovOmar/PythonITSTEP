#!C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe

import os

def send_redirect( location:str ) :
    print( "Status: 302 Found" )
    print( f"Location: {location}" )
    print()
    exit()

# Розбираємо рядок QUERY_STRING на dict
query_params = { k: v for k, v in ( pair.split('=') for pair in os.environ['QUERY_STRING'].split('&') ) }

titles = {
    'uk': "Вітаємо у магазині",
    'en': "Welcome to shop",
    'de': "Willkommen beim Einkaufen"
}
lang = query_params.get( 'lang', 'uk' )   # query_params['lang'] if 'lang' in query_params else 'uk' 
if not lang in titles :
    send_redirect( "/uk/shop/" )

title = titles[ lang ]

print( "Content-Type: text/html; charset=utf-8" )
print( "Connection: close" )
print()   # порожній рядок - кінець заголовків
print( f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="cp1251">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CGI</title>
</head>
<body>
    <h1>{title}</h1>
    <p>{lang}</p>
</body>
</html>''' )