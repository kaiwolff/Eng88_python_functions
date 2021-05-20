class Calculator:
    #made them static methods so that I don't have to create an object.
    @staticmethod
    def add(value1,value2) : return value1 + value2

    def subtract(value1, value2): return value1 - value2

    def multiply(value1, value2) : return value1 * value2

    def divide(value1, value2) : return value1 / value2

    def divisible(value1, value2):
        if value2 == 0:
            return False
        elif value1 % value2 == 0:
            return True
        else:
            return False


#Test Case
print(Calculator.add(1,1))
print(Calculator.subtract(1,1))
print(Calculator.multiply(1,2))
print(Calculator.divisible(4,2))
print(Calculator.divisible(3,2))
print(Calculator.divisible(3,0))
print(Calculator.divide(4,2))