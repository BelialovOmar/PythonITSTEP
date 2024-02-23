# Основи ООП

class Point :                 
    x = 0                    
    y = 0                     
    
def demo1() -> None :          
    p1 = Point()               
    p2 = Point()               
    print(p1.x, p2.x, Point.x)
    Point.x = 10               
    print(p1.x, p2.x, Point.x) 
    p1.x = 20                  
    print(p1.x, p2.x, Point.x) 
    Point.x = 30               
    print(p1.x, p2.x, Point.x)  
    del p1.x                   
    print(p1.x, p2.x, Point.x) 


class Vector :                   # Для того щоб створити об'єктні поля необхідний
                                 # екземпляр (instance) об'єкту. Він з'являється у
    def __init__( self,          # конструкторі. У Python конструктор - спец. метод __init__
           x:float=0,            # На відміну від неявного this використовується явний self 
           y:float=0 ) -> None:  # self є першим параметром усіх методів, звернення до 
        self.x = x               # полів та інших методів мають починатись з self.
        self.y = y               # В силу відсутності перевантаження, "різницю" у 
                                 # конструкторах також реалізують значеннями за замовчанням
    def __str__(self) -> str:    # ~ ToString() - викликається при виводі, у рядкових
        return f"({self.x}, {self.y})"  # операціях та приведення до рядкового типу

    def __repr__(self) -> str:   # representation - аналог __str__ але для "строгого" виведення
        return f"<Vector>({self.x}, {self.y})"
    
    def __add__(self, other) :   # "перевантаження" операторів - опис спец. методів.
        if isinstance( other, Vector ) :
            return Vector( self.x + other.x, self.y + other.y )
        else :
            raise ValueError( "Incompatable type: Vector required" )
        
    def __mul__(self, other) :     # демонструємо операції з різними типами
        if isinstance( other, (int, float) ) :   # множення вектора на число
            return Vector( self.x * other, self.y * other )
        elif isinstance( other, Vector ) :       # скалярне множення вектора на вектор
            return self.x * other.x + self.y * other.y
        else :
            raise ValueError( "Incompatable type: Vector or number required" )
    
    def magnitude(self) -> float :
        return (self.x * self.x + self.y * self.y) ** (1/2)

    def translate(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy



def demo2() -> None :
    v1 = Vector()
    v2 = Vector( 1 )
    v3 = Vector( 1, -1 )
    v4 = Vector( y=-1 )
    print(v3, v4, v3 + v4 )
    print( v3.magnitude() )    # при виклику метода self пропускається
    v3.translate(0.1, 0.2)
    print( "v3 translated =", v3 )
    print( "v3 * 2 =", v3 * 2 )
    print( "v3 * v2 =", v3 * v2 )


def main() -> None :           # 
    demo2()                    # 


if __name__ == "__main__" :
    main()
