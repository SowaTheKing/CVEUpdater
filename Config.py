from Logger import Logger
from _datetime import datetime


class Config:

    logger = None
    path = None

    def __init__(self, path):
        self.path = path
        self.last_run = self.__load_last_run()
        self.logger = Logger(1)

    def __load_last_run(self):
        if self.path is None:
            self.logger.fatal("Path is set to None. Exiting...")
            pass
        try:
            buffer = open(self.path).read()
            return datetime(int(buffer[:4]),
                            int(buffer[5:7]),
                            int(buffer[8:10]),
                            int(buffer[11:13]),
                            int(buffer[14:16]),
                            int(buffer[17:19]))
        except IOError:
            self.logger.fatal("Error while opening {0}!".format(self.path))
            pass

    def save_last_run(self):
        if self.path is None:
            self.logger.fatal("Path is set to None. Exiting...")
            pass
        try:
            file = open(self.path, "w")
            file.write(str(datetime.now()))
        except IOError:
            self.logger.fatal("Error while saving datetime to {0}".format(self.path))

