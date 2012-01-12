# -*- coding: UTF-8 -*-
import logging
from testfixtures.logcapture import log_capture
from simptools.decorators import catch_and_log_exception

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'

import unittest

class DecoratorsTestCase(unittest.TestCase):


    @catch_and_log_exception
    def div_by_zero(self):
        return 1/0

    @log_capture()
    def test_catch_and_log_exception(self, l):
        logger = logging.getLogger()
        self.div_by_zero()
        l.check(('root', 'ERROR', 'integer division or modulo by zero'),)


if __name__ == '__main__':
    unittest.main()
