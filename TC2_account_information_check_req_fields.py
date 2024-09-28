"""
TC2_account_information_check_req_fields : Testing new member enrollment page (Aeroplan)
Description : - This testcase is used to test the negative scenario.
              - Failing to provide required field values should prevent the user to navigate to the next
                section(Personal Information).
              - Appropriate validation messages should be displayed.
              - Required Fields are : Email address, password, checking the terms and conditions box (But this should be
                confirmed as per user requirement)
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def validate_required_fields(driver):
    # Not entering email address and password
    driver.find_element(By.NAME, "emailAddress").send_keys("")
    driver.find_element(By.NAME, "password").send_keys("")
    # click on continue
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//button[@role='button']"))
    msg1 = ""
    msg2 = ""
    msg3 = ""
    try:
        msg1 = driver.find_element(By.XPATH,
                                   "//mat-error[contains(normalize-space(),'Please enter your email address.')]").text
        msg2 = driver.find_element(By.XPATH, "//mat-error[contains(normalize-space(),'Please enter a password.')]").text
        msg3 = driver.find_element(By.XPATH,
                                   "//mat-error[contains(normalize-space(),'To continue, please tick the checkbox')]").text
        return True, msg1, msg2, msg3
    except NoSuchElementException:
        return False, msg1, msg2, msg3


if __name__ == '__main__':
    service = Service(executable_path="C:\\Driver\\Python_files\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get('https://www.aircanada.com/')
    driver.maximize_window()

    # click on Join Aeroplan button
    driver.find_element(By.ID, 'libraUserMenu-joinNow').click()

    status, act_msg1, act_msg2, act_msg3 = validate_required_fields(driver)

    assert status, " Test case 2 failed! - Able to continue to next section without entering required fields"

    print("Test case 2 Passed! - Not able to continue to next section without entering required fields")
    print(act_msg1)
    print(act_msg2)
    print(act_msg3)
