"""
TC3_search_bar_with_search_results: Testing Search bar
Description : - This testcase is used to test search bar and see if the results are displayed
              - Searches which yield results will be displayed (first page)
              - The links of the search result on the first search page will be returned

"""

from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def validate_search_bar(driver):
    driver.find_element(By.XPATH, "//input[@name='acSiteSearchInput']").send_keys("canada")
    driver.find_element(By.XPATH, "//input[@name='acSiteSearchInput']").send_keys(Keys.ENTER)
    search_result = []
    try:
        sr = driver.find_elements(By.XPATH, "//ol[@class='search-list simple-list']//a")
        for s in sr:
            search_result.append(s.text)
        return search_result
    except NoSuchElementException:
        return []


if __name__ == '__main__':
    service = Service(executable_path="C:\\Driver\\Python_files\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get('https://www.aircanada.com/')
    driver.maximize_window()

    search_results = validate_search_bar(driver)

    print(search_results)

