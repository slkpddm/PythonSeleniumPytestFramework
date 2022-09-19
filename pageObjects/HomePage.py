from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage



class HomePage():
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[@href='/angularpractice/shop']")
    name = (By.NAME,"name")
    email= (By.NAME,"email")
    password = (By.CSS_SELECTOR,"#exampleInputPassword1")
    gender = (By.CSS_SELECTOR,"#exampleFormControlSelect1")
    emp_status = (By.CSS_SELECTOR,"#inlineRadio1")
    dob = (By.NAME,"bday")
    submit = (By.CSS_SELECTOR,".btn-success")
    alert = (By.CSS_SELECTOR,".alert-success")
    def getHomePage(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckoutPage(self.driver)

    def name1(self):
        return self.driver.find_element(*HomePage.name)

    def email1(self):
        return self.driver.find_element(*HomePage.email)

    def password1(self):
        return self.driver.find_element(*HomePage.password)

    def gender1(self):
        return self.driver.find_element(*HomePage.gender)

    def empStatus(self):
        return self.driver.find_element(*HomePage.emp_status)

    def dateOfBirth(self):
        return self.driver.find_element(*HomePage.dob)

    def submit1(self):
        return self.driver.find_element(*HomePage.submit)

    def alertMsg(self):
        return self.driver.find_element(*HomePage.alert)


