def double(x):
    result = x*2
    return result

def add_five(x):
    result = x+5
    return result

def square(x):
    result = x**2
    return result

result = square(add_five(double(2)))
print(result)

def process(x):
        try:
            if x % 2 == 0:
                result = ((double(x)) ** 2)
                return result
            if x % 2 != 0:
                result = ((add_five(x)) ** 2)
                return result
        except TypeError:
             print("Пожалуйста, напишите число!")
        except FileNotFoundError:
             print("Похоже, тут типичное "f'404'"")
             
print(process("vpered"))
print(process(5))
print(process(2))