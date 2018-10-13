class Logger:
    """
    Levels:
    1 - log debug info
    2 - only info
    """
    level = 1

    def __init__(self, level):
        self.level = level

    def fatal(self, string):
        if self.level >= 1:
            print("[*****]" + string)

    def error(self, string):
        if self.level >= 2:
            print("[****]" + string)

    def warning(self, string):
        if self.level >= 3:
            print("[***]" + string)

    def info(self, string):
        if self.level >= 4:
            print("[**]" + string)

    def debug(self, string):
        if self.level >= 5:
            print("[*]" + string)
