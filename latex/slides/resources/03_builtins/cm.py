class MyManager:
    def __enter__(self):
        # tue dinge
        return self

    def __exit__(self, type, value, traceback):
        # schliesse handler etc ...
        pass

    def do_things(self):
        # ...
        pass

with MyManager() as m:
    m.do_things()
