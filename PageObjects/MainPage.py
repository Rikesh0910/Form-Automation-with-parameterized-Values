from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    firstname = (By.ID, "firstName")
    lastname = (By.ID, "lastName")
    email = (By.ID, "userEmail")
    male = (By.XPATH, "//label[@for='gender-radio-1']")
    mobile = (By.ID, "userNumber")
    subject = (By.XPATH, "//input[@id='subjectsInput']")
    hobbie = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
    address = (By.ID, "currentAddress")
    submit = (By.XPATH, "//button[@type='submit']")


    def get_first_name(self):
        return self.driver.find_element(*MainPage.firstname)

    def get_last_name(self):
        return self.driver.find_element(*MainPage.lastname)

    def get_email(self):
        return self.driver.find_element(*MainPage.email)

    def get_gender(self):
        return self.driver.find_element(*MainPage.male)

    def get_mobile(self):
        return self.driver.find_element(*MainPage.mobile)

    def get_subject(self):
        return self.driver.find_element(*MainPage.subject)

    def get_hobbie(self):
        return self.driver.find_element(*MainPage.hobbie)

    def get_address(self):
        return self.driver.find_element(*MainPage.address)


    def submit_form(self):
        return self.driver.find_element(*MainPage.submit)