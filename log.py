import loguru
import sys

# import sys


class Log:
    def __init__(self, level="DEBUG", log_path="log", to_file=False):
        # fmt_time = "{time:YYYY-MM-DD HH:mm:ss}"
        # fmt = f"{fmt_time}{sep}{level}{message}"
        # fmt = "{time: HH:mm:ss} -- {name} -- {level} -- {message}"
        # fmt = "{time: HH:mm:ss} --{level} -- {name} -- {message}"

        self.logger = loguru.logger
        self.logger.remove()

        self.logger.add(sys.stdout, level=level, colorize=True)
        if to_file:
            # remove default logger so you can set a stdout logger or the console will print twice for each log
            self.logger.add(log_path, level=level)


logger = Log().logger
