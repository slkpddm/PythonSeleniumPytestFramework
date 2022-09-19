from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

      def test_e2e(self):
          log = self.getLogger()
          homePage = HomePage(self.driver)
          checkoutPage = homePage.getHomePage()
          #checkoutPage = CheckoutPage(self.driver)
          log.info("All items list")
          products = checkoutPage.getItems()

          for product in products:
              if product.find_element(By.XPATH, "div/h4").text == "Blackberry":
                  product.find_element(By.XPATH, "div/button").click()
          checkoutPage.checkout1().click()
          confirm = checkoutPage.checoutNext1()
          #confirm = ConfirmPage(self.driver)
          log.info("Delvery location is India")
          confirm.getDeliveryLocation().send_keys("Ind")
          self.explicitWaiter("India")
          confirm.setLocation().click()
          confirm.checbox1().click()
          confirm.purchase1().click()
          msg = confirm.msgAlert().text
          log.info(msg)
          assert "Success! Thank you!" in msg
          #log.info(assert "Success! Thank you!" in msg)