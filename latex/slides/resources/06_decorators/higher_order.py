# def greet(name):
#     return "Hello {0}".format(name)

class GreetFunction:
    # wird beim Funktionsaufruf aufgerufen
    def __call__(self, name):
        return "Hello {0}".format(name)

greet = GreetFunction()

# Hello World
print(greet("World"))

# gibt Fizz wenn die Zahl durch 3 und Buzz
# wenn die Zahl durch 5 teilbar ist zurück
def fizzbuzz(number):
    teilbar_3 = number % 3 == 0
    teilbar_5 = number % 5 == 0
    if teilbar_3 and teilbar_5:
        return "FizzBuzz"
    elif teilbar_3:
        return "Fizz"
    elif teilbar_5:
        return "Buzz"
    else:
        return number

# gibt FizzBuzz, 1, 2, Fizz, 4, Buzz, Fizz, 7, 8 und Fizz aus
for number in map(fizzbuzz, range(0, 10)):
    print(number)

# gibt zurück ob eine Zahl gerade ist
def even(number):
    return number % 2 == 0

# gibt die Zahlen 0, 2, 4, 6 und 8 aus
for number in filter(even, range(0, 10)):
    print(number)
