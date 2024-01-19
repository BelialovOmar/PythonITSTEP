# Робота з базами даних на прикладі MySQL
# 
# 1. Створюємо БД
# 2. Налаштовуємо драйвер
# 3. Підключаємось
# 4. Виконуємо команди SQL, обробляємо відповіді
# 
# 1. Створюємо БД, користувача, права доступу
#  - при роботі з локальними СУБД, до яких є повний доступ,
#     дуже бажано створювати окремих користувачів для різних проєктів
#     та обмежувати їх права заданими БД. Це упереджує випадкові
#     пошкодження "не своїх" БД, а також спрощує розуміння які БД
#     належать до яких проєктів.
#  - БД 
#     через терминал  cd /xampp, потом cd mysql/bin
#     CREATE DATABASE py202 ;
#  - Користувач
#     CREATE USER py202_user@localhost IDENTIFIED BY 'pass_202' ;
#  - Права доступу
#     GRANT ALL PRIVILEGES ON py202.* TO py202_user@localhost ;
#  - Перевіряємо
#     Виходимо з консолі СУБД та заходимо під новим логіном/паролем
#     ./mysql -P 3306 -u py202_user -p'pass_202'
#
# 2. Драйвер
#  Драйвер підбирається під пару - СУБД та мова програмування (
#   середовище виконання). Встановлюємо командою (у терміналі)
#   pip install mysql-connector-python
#  Перевіряємо імпортом
import mysql.connector
import hashlib

def main() -> None:
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
    db_connection = None

    try:
        db_connection = mysql.connector.connect(**db_ini)
        print("Connection OK")
        
        sql = "SHOW DATABASES"
        with db_connection.cursor() as cursor:
            cursor.execute(sql)
            print(cursor.column_names)
            for row in cursor:
                print(row)
    except mysql.connector.Error as err:
        print(err)
    finally:
        if db_connection:
            db_connection.close()

if __name__ == "__main__":
    main()
