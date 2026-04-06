from driver_setup import setup_driver
from signin import signin_page, forget_pw
from crm import crm, ind_leads, business_leads, individual_leads, bus_leads, create_company, quotations
from sales_and_order import sales_and_order
from selenium.webdriver.common.by import By
import time

def complete_test():
    driver = setup_driver()

    try:
        signin_page(driver)
        #forget_pw(driver)
        #crm(driver)
        #ind_leads(driver)
        #create_company(driver)
        #bus_leads(driver)
        #individual_leads(driver)
        #business_leads(driver)
        #quotations(driver)
        #sales_and_order(driver)

        time.sleep(10)

    except Exception as e:
        print("Test failed:", str(e))

    finally:
        driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    complete_test()

