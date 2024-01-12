import json

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        # Представлення об'єкта у формі рядка
        return f"[{self.numerator}/{self.denominator}]"

    def __add__(self, other):
        # Додавання двох дробів
#        if isinstance(other, Fraction):
#            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
#            new_denominator = self.denominator * other.denominator
#            return Fraction(new_numerator, new_denominator)
#        else:
#            raise TypeError("Can only add Fraction to Fraction")
        return Fraction(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator
        )

    def __sub__(self, other):
        # Віднімання дробів
        return Fraction(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator
        )

    def __mul__(self, other):
        # Множення дробів
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __div__(self, other):
        # Ділення дробів
        return Fraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )

    def toJSON(self):
        # Представлення об'єкта у форматі JSON
        return json.dumps({"numerator": self.numerator, "denominator": self.denominator})

    def fromJSON(json_str):
        # Створення об'єкта з JSON
        try:
            data = json.loads(json_str)
            if "numerator" in data and "denominator" in data:
                return Fraction(data["numerator"], data["denominator"])
            else:
                raise ValueError("Invalid JSON format")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON")

    def reduce(self):
        # Скорочення дробу
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        greatest_common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= greatest_common_divisor
        self.denominator //= greatest_common_divisor
        return self

    def saveFile(self, filename):
        # Збереження об'єкта у файл
        with open(filename, 'w') as file:
            file.write(self.toJSON())

    def load(filename):
        # Відновлення об'єкта з файлу
        try:
            with open(filename, 'r') as file:
                json_str = file.read()
                return Fraction.fromJSON(json_str)
        except IOError as err:
            raise err

def main():
#    print("Enter the numerator of the first fraction: ")
#     f1n = int(input())
#     print("Enter the denominator of the first fraction: ")
#     f1d = int(input())
#     print("Enter the numerator of the second fraction: ")
#     f2n = int(input())
#     print("Enter the denominator of the second fraction: ")
#     f2d = int(input())
# 
#     f1 = Fraction(f1n, f1d)
#     f2 = Fraction(f2n, f2d)

#     print(f"f1 + f2 = {f1 + f2}")
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    print(f"f1 + f2 = {f1 + f2}")
    f1.saveFile("fraction.json")
    loaded_fraction = Fraction.load("fraction.json")
    print(f"Loaded fraction: {loaded_fraction}")
    reduced_fraction = loaded_fraction.reduce()
    print(f"Reduced fraction: {reduced_fraction}")

if __name__ == "__main__":
    main()
