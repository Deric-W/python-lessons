class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return '{} mit nachricht {}'.format(self.__class__, self.message)

try:
    # code
    raise KeyError('message')
# mit nur einer exception
# except MyException as error:
except (KeyError, MyException) as error:
    print(error)
    pass
else:
    # wird nur ausgeführt falls keine Exceptions auftreten
    print("not gonna happen")
finally:
    # was unbedingt zu tun ist
