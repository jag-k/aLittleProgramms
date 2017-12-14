class Reprint:
    def __init__(self, title=''):
        from sys import stdout
        self.w = stdout.write
        self.w(str(title))

    def __call__(self, *args, sep=' '):
        self.w('\r' + sep.join(map(str, args)))
        return self

    def clear(self):
        self.w('\r\r')
        return self

    def sleep(self, seconds):
        from time import sleep
        sleep(seconds)
        return self


"""
p = Reprint()
p("3…").sleep(1)
p("2…").sleep(1)
p("1…").sleep(1).clear()
print("GO!")
"""