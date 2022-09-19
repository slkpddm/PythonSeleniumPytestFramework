from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
      def __init__(self,driver):
          self.driver = driver
      cards = (By.XPATH,"//div[@class='card h-100']")

      def getItems(self):
          return self.driver.find_elements(*CheckoutPage.cards)

      checkout = (By.XPATH,"//a[@class='nav-link btn btn-primary']")
      def checkout1(self):
          return self.driver.find_element(*CheckoutPage.checkout)

      checkoutNext = (By.CSS_SELECTOR,".btn.btn-success")
      def checoutNext1(self):
          self.driver.find_element(*CheckoutPage.checkoutNext).click()
          return ConfirmPage(self.driver)

