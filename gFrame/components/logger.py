import logging
class Logger():
    def __init__(self, logger: bool = True, endReport: bool = False) -> None:
        self.logger = logger
        self.endReport = endReport