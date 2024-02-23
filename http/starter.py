import inspect
import time
import uuid
import appsettings
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import importlib
import os
import sys
sys.path.append(appsettings.CONTROLLERS_PATH)

class MainHandler(BaseHTTPRequestHandler):
    sessions = dict()

    def do_GET(self) -> None:
        # Розбір URL
        url_parts = self.path.split('?')
        if len(url_parts) > 2:
            self.send_404()
            return
        path = url_parts[0]
        query_string = url_parts[1] if len(url_parts) > 1 else None

        # Перевірка на існування статичного файлу
        filename = f"{appsettings.WWWROOT_PATH}/{path}"
        if os.path.isfile(filename):
            self.flush_file(filename)
            return

        # Робота з Cookie
        self.response_headers = dict()
        self.cookies = dict( ( cookie.split('=') for cookie in 
                    self.headers['Cookie'].split('; ') ) ) if 'Cookie' in self.headers else {}
        
        # Робота з сесіями
        session_id = self.cookies['session-id'] if 'session-id' in self.cookies else str( uuid.uuid1() )
        if not session_id in MainHandler.sessions:
            MainHandler.sessions[session_id] = {
                'timestamp': time.time(),
                'session-id': session_id
            }
            self.response_headers['Set-Cookie'] = f'session-id={session_id}'

        self.session = MainHandler.sessions[session_id]

        # Розбір шляху на контролер і дію
        path_parts = path.split('/')
        controller_name = (path_parts[1].capitalize() if path_parts[1] != '' else 'Home') + 'Controller'
        action_name = path_parts[2].lower() if len(path_parts) > 2 and path_parts[2] != '' else 'index'

        # Логування запиту
        print(f"Запит: {self.path}")
        print(f"Контролер: {controller_name}, Дія: {action_name}")

        try:
            controller_module = importlib.import_module(controller_name)
            controller_class = getattr(controller_module, controller_name)
            controller_object = controller_class(handler=self)
            controller_action = getattr(controller_object, action_name)
        except Exception as err:
            print(err)
            self.send_404()
            return

        if controller_action:
            controller_action()
        else:
            self.send_404()

def main() -> None :
    server = ThreadingHTTPServer( ( '127.0.0.1', 82 ), MainHandler )
    try :
        print( 'Server starting...' )
        server.serve_forever()
    except :
        print( 'Server stopped' )


if __name__ == "__main__" :
    main()
