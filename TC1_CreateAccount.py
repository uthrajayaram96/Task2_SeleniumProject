from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Entering account information - email, password, accepting terma and condition, selecting Areoplan number option (N0)
def enter_account_information(driver):
    # selecting Areoplan number option (N0)
    driver.find_element(By.XPATH, "(//label[@class='mat-radio-label'])[1]")

    driver.find_element(By.NAME, "emailAddress").send_keys("uthrajayaram02@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("TestPassword#1")
    # I was getting intercepted exception, so had to use execute script (JS) to identify the element
    driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "checkBox-input"))

    # click on continue
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//button[@role='button']"))
    return driver


# Entering Personal Information - Firstname, lastname, gender, language, birthday, month, year
def enter_personal_information(driver):
    driver.find_element(By.NAME, "firstName").send_keys("Uthra Jayaram")
    driver.find_element(By.NAME, "lastName").send_keys("Srinivasan")
    # Getting the gender options and selecting female option
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//div[@id='mat-select-value-3']"))
    all_aval_gender = driver.find_elements(By.XPATH, "//div[@role='listbox']//mat-option")
    for gender in all_aval_gender:
        # print(gender.text)
        if gender.text.lower() == 'female':
            driver.execute_script("arguments[0].click();", gender)
            break

    driver.execute_script("arguments[0].click();",
                          driver.find_element(By.XPATH, "(//div[contains(@class,'mat-select-trigger')])[2]"))
    all_aval_languages = driver.find_elements(By.XPATH, "//div[@aria-label='Preferred language']//mat-option")
    for language in all_aval_languages:
        # print(language.text)
        if language.text.lower() == 'english':
            driver.execute_script("arguments[0].click();", language)
            break
    # Select month
    driver.execute_script("arguments[0].click();",
                          driver.find_element(By.XPATH, "(//div[contains(@class,'mat-select-trigger')])[4]"))
    months = driver.find_elements(By.XPATH, "//div[contains(@aria-label,'Month.')]//mat-option")
    for month in months:
        if month.text.lower() == 'feb':
            driver.execute_script("arguments[0].click();", month)
            break
    # Select Year
    driver.execute_script("arguments[0].click();",
                          driver.find_element(By.XPATH, "(//div[contains(@class,'mat-select-trigger')])[5]"))
    years = driver.find_elements(By.XPATH, "//div[contains(@aria-label,'Year.')]//mat-option")
    for year in years:
        if year.text == '1996':
            driver.execute_script("arguments[0].click();", year)
            break
    # select Day
    driver.execute_script("arguments[0].click();",
                          driver.find_element(By.XPATH, "(//div[contains(@class,'mat-select-trigger')])[3]"))
    days = driver.find_elements(By.XPATH, "//div[contains(@aria-label,'Day')]//mat-option")
    for day in days:
        if day.text == '12':
            driver.execute_script("arguments[0].click();", day)
            break

    # click on continue
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//button[@role='button']"))
    return driver


# Entering Contact Information - Entering address line 1, city, postal code, state, country, phone numer,
# accepting privacy policy
def enter_contact_information(driver):
    driver.find_element(By.XPATH, "//input[@formcontrolname='addressLine1']").send_keys("2107 Deer Creek Dr")
    driver.find_element(By.XPATH, "//input[@formcontrolname='city']").send_keys("Plainsboro")
    # Select country
    #driver.execute_script("arguments[0].click();",
                          #driver.find_element(By.XPATH, "(//div[contains(@class,'mat-select-trigger')])[1]"))
    #driver.find_element(By.XPATH, "(//div[contains(@class,'mat-select-trigger')])[1]").click()
    #driver.find_element(By.XPATH,"//mat-select[@name='country']").click()

    # had to use explicit wait
    country_ele = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//mat-select[@name='country']")))
    country_ele.click()
    countries = driver.find_elements(By.XPATH, "//div[@aria-label='Country/Region']//mat-option")
    print(len(countries))
    for country in countries:
        if country.text.lower() == 'united states':
            driver.execute_script("arguments[0].click();", country)
            break
    # Select State
    driver.execute_script("arguments[0].click();",
                          driver.find_element(By.XPATH, "(//div[contains(@class,'mat-select-trigger')])[2]"))
    states = driver.find_elements(By.XPATH, "//div[@aria-label='State']//mat-option")
    for state in states:
        if state.text.lower() == 'new jersey':
            driver.execute_script("arguments[0].click();", state)
            break
    # Select Country code
    driver.execute_script("arguments[0].click();",
                          driver.find_element(By.XPATH, "(//div[contains(@class,'mat-select-trigger')])[3]"))
    country_codes = driver.find_elements(By.XPATH, "//div[@aria-label='Phone number']//span[@class='country-name']")
    for cc in country_codes:
        if cc.text.lower() == "united states":
            driver.execute_script("arguments[0].click();", cc)
            break
    driver.find_element(By.XPATH, "//input[@formcontrolname='zip']").send_keys("08536")
    driver.find_element(By.XPATH, "//input[@formcontrolname='phoneNumber']").send_keys("7085632158")
    driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "privacyPolicycheckBox-input"))
    return driver


if __name__ == '__main__':
    service = Service(executable_path="C:\\Driver\\Python_files\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(20)
    driver.get('https://www.aircanada.com/')
    driver.maximize_window()

    # click on Join Aeroplan button
    driver.find_element(By.ID, 'libraUserMenu-joinNow').click()

    driver = enter_account_information(driver)
    driver = enter_personal_information(driver)
    driver = enter_contact_information(driver)
