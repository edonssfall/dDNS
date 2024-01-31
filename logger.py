import datetime
import os


class Logger:
    def __init__(self, name="logger"):
        self.name = name
        self.stamp = datetime.datetime.now().isoformat()
        self.path = os.path.join(os.getcwd(), "logs", f"{name}_{self.stamp}.log")
        if not os.path.exists(os.path.dirname(self.path)):
            os.makedirs(os.path.dirname(self.path))
        self.file = open(self.path, "a")

    def log(self, level, message):
        self.file.write(f"[{level}] {datetime.datetime.now().isoformat()} - {message}\n")
        self.file.close()
