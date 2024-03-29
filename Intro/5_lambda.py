# Лямбда-вираз: вираз, який повертає функцію

lam1 = None  # існує у глобальному контексті
lam2 = None
y = 30
w = 30

def init_lam1() :
    global lam1
    y = 10
    lam1 = lambda x : print( x, y )  # створюється у контексті init_lam1
    # при дефініції виявляється що існує посилання на "у", контекст якого локалізований
    # - не буде доступний при виклику (з main). Відбувається capture (closure/scoped)
    # - у capture group (лексикографічний окіл) функції додається "у" зі значенням 10


def init_lam2() :                    # Оголошення lam2 звертається до "w", яка залишається
    global lam2                      # доступною, оскільки є глобальною. Копія не створюється
    lam2 = lambda x : print( x, w )  # (capture не відбувається)


def oper( lam ) -> int :
    return lam( 1, 2 )


def main() -> None :
    global w
    init_lam1()       # на момент створення "у"=10, на момент виклику існують
    y = 20            # декілька "у" - 2 локальні: (main та init) та глобальний
    lam1( "Hello" )   # викликається з контексту main ?? який "у" буде у тілі lam1?

    init_lam2()       # на момент створення lam2  w = 30
    w = 20            # змінюємо w 
    lam2( "Hello" )   # lam2 звертається до глобальної "w" але яке значення буде:
                      # 30, яке було при створенні lam2 (30), або на час виклику (20)
    lam3 = lambda x, y : print(x, y)
    lam3( 10, "asd" ) 
    lam4 = lambda : print( 'No params' )
    lam4()
    # Переваги лямбда-виразів
    # IIFE Immediately invoked functional expression - вирази миттєвого виклику
    ( lambda : print( "IIFE" ) )()  # одноразова дія без залишку у пам'яті
    # створення множин з функцій, передача їх до інших функцій, патерн "Стратегія"
    print( oper( lambda x, y : x + y ) )
    print( oper( lambda x, y : x - y ) )

if __name__ == "__main__" :
    main()
