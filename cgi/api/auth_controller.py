import api_controller
import sys
sys.path.append('../../')
import db_ini
import base64
import hashlib
import mysql.connector

class AuthController(api_controller.ApiController):

    def connect_db_or_exit(self):
        if not self.db_connection:
            try:
                self.db_connection = mysql.connector.connect(**db_ini.connection_params)
            except mysql.connector.Error as err:
                self.send_response(500, "Internal Server Error", {"message": str(err)})
        return self.db_connection

    def do_get(self):
        try:
            auth_token = self.get_auth_header_or_exit()
            login, password = base64.b64decode(auth_token, validate=True).decode().split(':', 1)

            sql = "SELECT u.* FROM users u WHERE u.`login`=%s AND u.`password`=%s"
            with self.connect_db_or_exit().cursor() as cursor:
                cursor.execute(sql, (login, hashlib.md5(password.encode()).hexdigest()))
                row = cursor.fetchone()
                if row is None:
                    self.send_response(401, "Unauthorized", meta={"message": "Credentials rejected"})
                user_data = dict(zip(cursor.column_names, row))
                self.send_response(meta={"scheme": "Bearer"}, data={"token": str(user_data['id'])})
        except Exception as e:
            self.send_response(401, "Unauthorized", meta={"message": str(e)})


def do_post(self):
    try:
        token = self.get_bearer_token_or_exit()
        self.send_response(meta={"message": "Token is valid"}, data={"token": token})
    except Exception as e:
        self.send_response(401, "Unauthorized", meta={"message": str(e)})
