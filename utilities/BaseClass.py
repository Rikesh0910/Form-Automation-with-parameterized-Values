import inspect
import logging

import pytest

from FormTestData.Form_test_data import FormTestData


@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    @pytest.fixture(params=FormTestData.data)
    def getData(self, request):
        return request.param