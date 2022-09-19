import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



@pytest.mark.usefixtures("setup")
class BaseClass:


      def explicitWaiter(self,country):
          wait = WebDriverWait(self.driver, 10)
          wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,country)))

      def getLogger(self):
          loggerName = inspect.stack()[1][3]
          logger = logging.getLogger(loggerName)
          fileHandler = logging.FileHandler("pytest.log")
          Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
          fileHandler.setFormatter(Formatter)
          logger.addHandler(fileHandler)
          logger.setLevel(logging.DEBUG)
          return logger