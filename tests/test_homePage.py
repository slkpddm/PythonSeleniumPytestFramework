import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from testData.homePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
      def test_loginPage(self,getData):
          log = self.getLogger()
          homePage = HomePage(self.driver)
          log.info("Name is "+getData['name'])
          homePage.name1().send_keys(getData["name"])
          log.info("Email is"+getData['email'])
          homePage.email1().send_keys(getData["email"])
          log.info("password is"+getData['password'])
          homePage.password1().send_keys(getData["password"])
          log.info("Gendor is "+getData['gender'])
          homePage.gender1().send_keys(getData["gender"])
          homePage.empStatus().click()
          log.info("DateOfBirth is"+getData['dob'])
          homePage.dateOfBirth().send_keys(getData["dob"])
          homePage.submit1().click()
          msg = homePage.alertMsg().text
          log.info(msg)
          assert "Success!" in msg
          self.driver.refresh()


      @pytest.fixture(params=HomePageData.test_data)
      def getData(self,request):
          return request.param