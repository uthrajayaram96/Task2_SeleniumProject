"""
TC4_search_bar_no_search_results: Testing Search bar
Description : - This testcase tests to see when search results yields no result a proper message is displayed
              - The message should adhere to the user requirement
              - "Your search - SERACH RESULT NAME - did not return any results. You may want to try entering different
                words or search using the navigation tabs at the top of this page."

"""

from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def validate_search_bar(driver, search_word):
    driver.find_element(By.XPATH, "//input[@name='acSiteSearchInput']").send_keys(search_word)
    driver.find_element(By.XPATH, "//input[@name='acSiteSearchInput']").send_keys(Keys.ENTER)

    try:
        no_search_result_found_msg = driver.find_element(By.XPATH,
                                                         "//strong[contains(normalize-space(),'did not return any results. You may want to try entering different words or search using the navigation tabs at the top of this page.')]").text
        return no_search_result_found_msg
    except NoSuchElementException:
        return ""


if __name__ == '__main__':
    service = Service(executable_path="C:\\Driver\\Python_files\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(30)
    driver.get('https://www.aircanada.com/')
    driver.maximize_window()
    search_word = 'GFFRTS'

    expected_msg = 'Your search - ' + search_word + ' - did not return any results. You may want to try entering different words or search using the navigation tabs at the top of this page.'
    actual_msg = validate_search_bar(driver, search_word)

    if actual_msg == expected_msg:
        print("Test case passed")
        print(actual_msg)
    else:
        assert False, "Test case failed - The expected message and actual message didn't match"
