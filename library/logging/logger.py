import logging
import sys

from .formatters import CustomFormatter
from .handlers import MakeFileHandler


class Logger:
    _log = None

    def __init__(self, name, filename=None, console_level='DEBUG', out_level='DEBUG'):
        self.__prepare_logger(name=name, filename=filename, console_level=console_level, out_level=out_level)

    def __prepare_logger(self, name, console_level, out_level, filename):
        assert console_level in {'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'}

        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(CustomFormatter())
        sh.setLevel(getattr(logging, console_level))

        Logger._log = logging.getLogger(name)
        Logger._log.setLevel(getattr(logging, console_level))
        Logger._log.addHandler(sh)

        if filename:
            fh = MakeFileHandler(filename, 'a+', 'utf-8')
            fh.setFormatter(logging.Formatter("%(asctime)s - [%(levelname).1s] %(name)s | (%(filename)s:%(lineno)d) - %(message)s"))
            fh.setLevel(getattr(logging, out_level))
            Logger._log.addHandler(fh)

    def get_logger(self):
        return Logger._log


def info(*args):
    return Logger._log.info(f'{" ".join(args)}')


def debug(*args):
    return Logger._log.debug(f'{" ".join(args)}')


def warning(*args):
    return Logger._log.warning(f'{" ".join(args)}')


def error(*args):
    return Logger._log.error(f'{" ".join(args)}')


def critical(*args):
    return Logger._log.critical(f'{" ".join(args)}')
