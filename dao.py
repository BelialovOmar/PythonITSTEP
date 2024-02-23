# Data access layer
import db_ini
import logging
import mysql.connector

db_connection = None
def connect_db() :
    global db_connection
    if not db_connection : 
        db_connection = mysql.connector.connect( **db_ini.connection_params )
    return db_connection


class Products :
    def get_all() :        
        ret = []
        sql = "SELECT * FROM products"
        try :
            db = connect_db()
            with db.cursor() as cursor :
                cursor.execute( sql )
                for row in cursor :
                    ret.append( dict( zip( cursor.column_names, map( str, row ) ) ) )
        except mysql.connector.Error as err :
            logging.error( 'SQL error', { 'sql': sql, 'err': err } )
            raise RuntimeError()
        except Exception as err :
            logging.error( 'Exception', { 'err': str( err ) } )
            raise RuntimeError()
        else :
            return ret
        
    def add( product:dict ) :
        try :
            db = connect_db()
            sql = "INSERT INTO products (`name`, `price`, `image_url`) VALUES ( %(name)s, %(price)s, %(image)s )"        
            with db.cursor() as cursor :
                cursor.execute( sql, product )
            db.commit()   # завершити транзакцію
        except mysql.connector.Error as err :
            logging.error( 'SQL error', { 'sql': sql, 'err': err } )
            raise RuntimeError()
        except Exception as err :
            logging.error( 'Exception', { 'err': str( err ) } )
            raise RuntimeError()


class Cart:
    @staticmethod
    def add(cart_item: dict):
        db = connect_db()
        try:
            check_sql = "SELECT cnt FROM cart WHERE id_user=%s AND id_product=%s"
            with db.cursor() as cursor:
                cursor.execute(check_sql, (cart_item['id_user'], cart_item['id_product']))
                result = cursor.fetchone()

            if result:
                new_cnt = result[0] + 1
                update_sql = "UPDATE cart SET cnt=%s WHERE id_user=%s AND id_product=%s"
                cursor.execute(update_sql, (new_cnt, cart_item['id_user'], cart_item['id_product']))
            else:
                insert_sql = "INSERT INTO cart (id_user, id_product, cnt) VALUES (%s, %s, 1)"
                cursor.execute(insert_sql, (cart_item['id_user'], cart_item['id_product']))

            db.commit() 
        except mysql.connector.Error as err:
            logging.error('SQL error', {'sql': sql, 'err': err})
            raise RuntimeError()
        except Exception as err:
            logging.error('Exception', {'err': str(err)})
            raise RuntimeError()


class Auth :
    def get_user_id_by_token( token:str ) -> str | None :
        # token це і є ід користувача, але перевіряємо у БД
        sql = "SELECT COUNT(u.id) FROM users u WHERE u.id=%s"
        try :
            db = connect_db()
            with db.cursor() as cursor :
                cursor.execute( sql, ( token, ) )
                cnt = cursor.fetchone()[0]
        except mysql.connector.Error as err :
            logging.error('SQL error', {'sql': sql, 'err': err})
            raise RuntimeError( str(err) )
        except Exception as err :
            logging.error('Exception', {'err': err})
            raise RuntimeError( str(err) )
        else :
            return token if cnt == 1 or cnt == "1" else None


