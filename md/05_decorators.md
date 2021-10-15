# Funktionen höherer Ordnung

## Funktionen sind Objekte


Funktionen sind Objekte mit speziellen Methoden.

```python
# def greet(name):
#     return "Hello {0}".format(name)

class GreetFunction:
    # wird beim Funktionsaufruf aufgerufen
    def __call__(self, name):
        return "Hello {0}".format(name)

greet = GreetFunction()

# Hello World
print(greet("World"))
```

---

## Folgen


-   Funktionen können Variablen zugewiesen werden,

```python
# Funktionen Variablen zuweisen
def return_hello():
    return "Hello"

say_hello = return_hello

print(say_hello())
# => Hello
```

---

-   Sie können in Funktionen definiert werden,

```python
# Funktionen in Funktionen definieren
def greet(name):
    def return_hello():
        return "Hello "
    greeting = return_hello() + name
    return greeting

print(greet("World"))
# => Hello World
```

---

-   Sie können andere Funktionen zurückgeben,

```python
# Rueckgabe von Funktionen
def greet():
    def say_hello():
        return "Hello"
    return say_hello

print(greet()())
# Hello
```

---

-   Sie können als Parameter mitgegeben werden

```python
# Uebergabe von Funktionen
def say_date(date):
    return "Today it's {date}".format(date=date)

def which_date(function):
    date = "25th June 2015"
    return function(date)

print(which_date(say_date))
# => Today it's 25th June 2015
```

---

## Beispiele - map


`map(function, iterable)` wendet eine Funktion auf alle Elemente eines Iterators an.

```python
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
```

---

## Beispiele - filter

`filter(function, iterable)` gibt die Elemente eines Iterators zurück, für welche die Funktion `True` zurückgibt.

```python
# gibt zurück ob eine Zahl gerade ist
def even(number):
    return number % 2 == 0

# gibt die Zahlen 0, 2, 4, 6 und 8 aus
for number in filter(even, range(0, 10)):
    print(number)
```

# Decorator

## einfache Decorator


Decorator sind Wrapper über existierende Funktionen.  
Dabei werden die zuvor genannten Eigenschaften verwendet.
Eine Funktion, die eine weitere als Argument hat, erstellt eine neue
Funktion.

---

```python
def get_date(date):
    return ", today it's {}.".format(date)


# unser decorator
def tell_the_world(func):
    def complete_sentence(date):
        return "Hello World{}".format(func(date))
    return complete_sentence
```

---

```python
# normaler Aufruf:
print(tell_the_world(get_date)("25th June 2015"))

# als decorator
get_date = tell_the_world(get_date)

print(get_date("25th June 2015"))
# => Hello World, today it's 25th June 2015.
```

---

Durch das `@` Symbol lässt sich der Decorator wesentlich einfacher verwenden.  
Es können auch mehrere Decorator übereinander geschrieben werden.

---

```python
# Nutzung des @ Syntaxes
def tell_the_world(func):
    def complete_sentence(date):
        return "Hello World, {}".format(func(date))
    return complete_sentence


@tell_the_world
def get_date(date):
    return "today it's {}.".format(date)

print(get_date("25th June 2015"))
# => Hello World, today it's 25th June 2015.
```

## Decorator mit Argumenten


Decorator erwarten Funktionen als
Argumente. Aus diesem Grund kann man nicht einfach andere Argumente
mitgeben, sondern man muss eine Funktion schreiben, die dann den
Decorator erstellt.

---

```python
# Decorator mit Argumenten
def tell_the_date_to(name):
    def name_decorator(func):
        def complete_sentence(date):
            return "Hello {name}, {date}".format(name=name,
                                                 date=func(date))
        return complete_sentence
    return name_decorator


@tell_the_date_to("John Doe")
def get_date(date):
    return "today it's {}.".format(date)

print(get_date("25th June 2015"))
# => Hello John Doe, today it's 25th June 2015.
```
