from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass


class Test_main(BaseClass):

    def test_form(self, getData):

        log = self.get_logger()
        log.info("the test starts!")
        main = MainPage(self.driver)
        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element(By.ID, "currentAddress")).perform()
        log.info("filling data into the form.")
        main.get_first_name().send_keys(getData["firstname"])
        log.info("firstname entered")
        main.get_last_name().send_keys(getData["lastname"])
        log.info("lastname entered")
        main.get_email().send_keys(getData["email"])
        log.info("email entered")
        main.get_gender().click()
        log.info("gender option clicked")
        main.get_mobile().send_keys(getData["mobile"])
        log.info("mobile no entered")
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//label[@for='hobbies-checkbox-1']")))
        main.get_hobbie().click()
        log.info("hobbie entered")
        main.get_address().send_keys(getData["address"])
        log.info("address entered")
        submit_button = main.submit_form()
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()
        log.info("submit form clicked!")

        self.driver.refresh()

