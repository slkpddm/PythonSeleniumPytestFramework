from selenium.webdriver.common.by import By


class ConfirmPage:
      def __init__(self,driver):
          self.driver = driver

      del_loc = (By.CSS_SELECTOR,"#country")
      def getDeliveryLocation(self):
          return self.driver.find_element(*ConfirmPage.del_loc)

      selLoc = (By.XPATH,"//div[@class='suggestions']/ul[1]")
      def setLocation(self):
          return self.driver.find_element(*ConfirmPage.selLoc)

      checkbox = (By.XPATH,"//label[@for='checkbox2']")
      def checbox1(self):
          return self.driver.find_element(*ConfirmPage.checkbox)

      purchase = (By.CSS_SELECTOR,"input[value='Purchase']")
      def purchase1(self):
          return self.driver.find_element(*ConfirmPage.purchase)

      message = (By.CSS_SELECTOR,".alert")
      def msgAlert(self):
          return  self.driver.find_element(*ConfirmPage.message)
