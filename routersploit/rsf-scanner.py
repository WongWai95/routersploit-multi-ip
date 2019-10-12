#!/usr/bin/env python3

from __future__ import print_function
import logging.handlers
import sys
if sys.version_info.major < 3:
    print("RouterSploit supports only Python3. Rerun application in Python3 environment.")
    exit(0)

from routersploit.non_interactive_scanner import RoutersploitInterpreter

log_handler = logging.handlers.RotatingFileHandler(filename="routersploit.log", maxBytes=500000)
log_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s       %(message)s")
log_handler.setFormatter(log_formatter)
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(log_handler)


def routersploit():
    rsf = RoutersploitInterpreter()
    rsf.start(sys.argv[1])


if __name__ == "__main__":
    routersploit()
