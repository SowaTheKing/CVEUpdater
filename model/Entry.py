from datetime import datetime


class Entry:
    def __init__(self, Modified, Published, cvss, cwe, id, last_modified, summary, vulnerable_configuration):
        self.last_modified = last_modified
        self.id = id
        self.summary = summary
        self.cwe = cwe
        self.cvss = cvss
        self.Published = Published
        self.Modified = Modified
        self.vulnerable_configuration = vulnerable_configuration

    def display(self):
        print("\n ID: {0}\n\nLAST MODIFIED {1}\nPUBLISHED: {2}\n\nINFO: {3}".format(self.id, self.last_modified,
                                                                                    self.Published, self.summary))

    def get_last_modified(self):
        year = self.last_modified[:4]
        month = self.last_modified[5:7]
        day = self.last_modified[8:10]
        hour = self.last_modified[11:13]
        minutes = self.last_modified[14:16]
        seconds = self.last_modified[17:19]
        return datetime(int(year), int(month), int(day), int(hour), int(minutes), int(seconds))