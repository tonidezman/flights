class Parser:
    def __init__(self, file, header, sep="^"):
        self.file = file
        self.header = header
        self.sep = sep

    def run(self):
        res = []
        with open(self.file) as f:
            for line in f:
                res.append(
                    dict(zip(self.header, line.strip().split(self.sep))))
        return res
