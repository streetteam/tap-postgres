import logging

import singer

LOGGER = singer.get_logger()
# temporarily set logging level to warning to prevent imported libraries spamming before level is
# properly set in __init__.py:main
LOGGER.setLevel(logging.WARNING)
