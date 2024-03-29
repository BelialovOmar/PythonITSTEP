import mysql.connector
import hashlib

db_ini = {
    'host': 'localhost',
    'port': 3307,
    'user': 'py202_user',
    'password': 'pass_202',
    'database': 'py202',
    'charset': 'utf8mb4',
    'use_unicode': True,
    'collation': 'utf8mb4_unicode_ci'
}
db_connection = None


def connect_db() :
    global db_connection
    try :
        db_connection = mysql.connector.connect( **db_ini )
    except mysql.connector.Error as err :
        print( err )
        return
    else :
        print( "Connection OK" )


def show_databases() :
    global db_connection
    sql = "SHOW DATABASES"
    try :
        with db_connection.cursor() as cursor :
            cursor.execute( sql )
            print( cursor.column_names )
            for row in cursor :
                print( row )
    except mysql.connector.Error as err :
        print( err )
        return     


def create_users() :
    global db_connection
    sql = """CREATE TABLE users (
    `id`       BIGINT UNSIGNED  PRIMARY KEY  DEFAULT (UUID_SHORT()),
    `login`    VARCHAR(32)   NOT NULL  UNIQUE,
    `password` CHAR(32)      NOT NULL,
    `avatar`   VARCHAR(256)  NULL
    ) ENGINE = InnoDB, DEFAULT CHARSET = utf8mb4 COLLATE utf8mb4_unicode_ci """
    try :
        with db_connection.cursor() as cursor :
            cursor.execute( sql )
    except mysql.connector.Error as err :
        print( err )
    else :
        print( 'CREATE TABLE users -- OK' )


def add_user( login:str, password:str, avatar:str=None ) :
    sql = "INSERT INTO users (`login`, `password`, `avatar`) VALUES ( %s, %s, %s )"
    password = hashlib.md5( password.encode() ).hexdigest()
    try :
        with db_connection.cursor() as cursor :
            cursor.execute( sql, ( login, password, avatar ) )
        db_connection.commit()   # завершити транзакцію
    except mysql.connector.Error as err :
        print( err )
    else :
        print( 'INSERT INTO users -- OK' )


def create_products() : 
    global db_connection
    sql = """CREATE TABLE products (
    `id`        BIGINT UNSIGNED  PRIMARY KEY  DEFAULT (UUID_SHORT()),
    `name`      VARCHAR(32)   NOT NULL,
    `price`     FLOAT         NOT NULL,
    `image_url` VARCHAR(256)  NULL
    ) ENGINE = InnoDB, DEFAULT CHARSET = utf8mb4 COLLATE utf8mb4_unicode_ci """
    try :
        with db_connection.cursor() as cursor :
            cursor.execute( sql )
    except mysql.connector.Error as err :
        print( err )
    else :
        print( 'CREATE TABLE products -- OK' )


def add_product( name:str, price:float, image_url:str=None ) :
    sql = "INSERT INTO products (`name`, `price`, `image_url`) VALUES ( %s, %s, %s )"
    try :
        with db_connection.cursor() as cursor :
            cursor.execute( sql, ( name, price, image_url ) )
        db_connection.commit()   # завершити транзакцію
    except mysql.connector.Error as err :
        print( err )
    else :
        print( 'INSERT INTO products -- OK' )


def create_cart() : 
    global db_connection
    sql = """CREATE TABLE cart (
    `id`         BIGINT UNSIGNED  PRIMARY KEY  DEFAULT (UUID_SHORT()),
    `id_user`    BIGINT UNSIGNED  NOT NULL,
    `id_product` BIGINT UNSIGNED  NOT NULL,
    `cnt`        INT              NOT NULL  DEFAULT 1
    ) ENGINE = InnoDB, DEFAULT CHARSET = utf8mb4 COLLATE utf8mb4_unicode_ci """
    try :
        with db_connection.cursor() as cursor :
            cursor.execute( sql )
    except mysql.connector.Error as err :
        print( err )
    else :
        print( 'CREATE TABLE cart -- OK' )



def main() -> None :
    connect_db()
    # create_users()
    user = {
        "login": "user",
        "password": "123",
        "avatar": "user1.png"
    }
    # add_user( **user )
    product = {
        "name": "Яблуко Фуджи",
        "price": 22.50,
        "image_url": "product1.png"
    }
    # create_products()
    # add_product( **product )
    create_cart()


if __name__ == "__main__" :
    main()

