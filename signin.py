from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def signin_page(driver):
    driver.maximize_window()
    driver.get("https://dek-crm.dev.geniussystems.com.np/")
    time.sleep(2)

    wait = WebDriverWait(driver, 10)

    sign_in = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@class='text-sm text-gray-600']")))
    if sign_in:
        print("Sign in to your account visible")
    time.sleep(2)

    email = driver.find_element(By.ID, "email")
    email.send_keys("abc@gmail.com")
    time.sleep(2)

    password = driver.find_element(By.XPATH, "//input[@type='password']")
    password.send_keys("abc")

    signin = driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']")
    signin.click()
    time.sleep(2)

    assert "/dashboard" in driver.current_url, "Not sign in"
    print("Sign in successful")

def forget_pw(driver):
    wait = WebDriverWait(driver, 10)

    sign_in = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@class='text-sm text-gray-600']")))
    if sign_in:
        print("Sign in to your account visible")
    time.sleep(2)

    email = driver.find_element(By.ID, "email")
    email.send_keys("reetithapa28@gmail.com")
    time.sleep(2)

    password = driver.find_element(By.XPATH, "//input[@type='password']")
    password.send_keys("Reeti@1234")

    signin = driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']")
    signin.click()
    time.sleep(2)
    invalid_pw = driver.find_element(By.XPATH, "//p[@class='text-xs text-red-600']")

    assert "Invalid login credentials" in invalid_pw.text, "Valid login credentials"

    forget_pw = driver.find_element(By.XPATH, "//button[normalize-space()='Forgot password?']")
    forget_pw.click()
    time.sleep(2)

    email = driver.find_element(By.XPATH, "//input[@class='w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-sm outline-none focus:ring-2 focus:ring-black/10']")
    email.send_keys("reetithapa28@gmail.com")
    time.sleep(2)

    send_link = driver.find_element(By.XPATH, "//button[normalize-space()='Send link']")
    send_link.click()


