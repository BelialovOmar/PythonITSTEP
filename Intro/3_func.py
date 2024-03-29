# Функції та видність змінних
x = 10  # глобальна змінна

def get_x() :  # casing: snake_case
    return x   # звернення до глобальної змінної


def hello( name:str="Anonym" ) -> str :   # зазначається тип параметру та значення за замовчанням
    '''Comment to function'''             # документуючий коментар - виводиться як підказка
    return f"Hello, {name}"               # -> str тип повернення


def change_x( value: int = 20 ) -> None :  # None (тут) - як аналог void
    x = value                              # !! це не звернення до глобальної змінної,
    print( "Changed to", x )               # а створення локальної


def set_x( value ) :        # ілюструємо, що зазначення типів - не вимагається
    global x                # зазначаємо, що під "х" розуміємо глобальну змінну
    x = value               # дана інструкція змінить саме глобальну змінну
    print( "Set to", x )    # 


def pair() :            # Повернення множинного значення
    return x, 2 * x     # 


def main() :
    print( "x = ", get_x() )
    print( hello(), hello( "User" ) )
    change_x( 1.5 )           # зазначення типу value:int не забороняє передавати інші дані
    print( "x = ", get_x() )
    set_x( value=30 )         # можна зазначати назву параметра
    print( "x = ", get_x() )

    y, w = pair()              # одержання множинного значення
    print( f"y={y}, w={w}" )   # ! не по-функціональному - розщеплюється кортеж 

    print( "y=%d, w=%d" % pair() )  # по-функціональному - кортеж зчеплюється з рядком



if __name__ == "__main__" : main()
