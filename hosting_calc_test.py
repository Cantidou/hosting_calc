import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

time.sleep(3)
options = webdriver.ChromeOptions()
options.set_capability("browserName", "chrome")
options.set_capability("browserVersion", "120.0")
driver = webdriver.Remote(command_executor='http://chrome:4444', options=options)
#http://172.17.0.2:4444 при запуске в докере
#http://localhost:4444 при запуске локально с подключением к гриду


class TestHostingPage:
    driver.get("https://gcore.com/hosting")
    driver.maximize_window()

    allure.step("Chooses servers Dedicated type")
    dedicated_server_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".gc-server-configurator-buttons button:nth-child(1)")))
    dedicated_server_button.click()

    allure.step("Chose the currency")
    currency_switcher = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".gc-switcher-toggler")))
    currency_switcher.click()


    price_inputs = driver.find_elements(By.CSS_SELECTOR, ".gc-input__number input")
    allure.step("Enter price min and max values")
    time.sleep(1)
    price_inputs[0].clear()
    price_inputs[0].send_keys(666)
    time.sleep(1)
    price_inputs[1].clear()
    price_inputs[1].send_keys(1000)

    show_more_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".gc-server-configurator-more")))
    show_more_btn.click()

    @allure.title("Search result test")
    @allure.description("Assert search result must contain:"
                        "1. Servers with price between min and max values entered at previous step"
                        "2. Server price currency is equal to chosen currency")
    def test_currencies_on_the_page(self):
        cards_price = driver.find_elements(By.CSS_SELECTOR, ".price-card_price")
        print(f"cards on the page {len(cards_price)}")
        for i in range(1, len(cards_price)):
            currency = cards_price[i].text.split(" ")[0]
            price = cards_price[i].text.split(" ")[1]

            with allure.step(f"Test card №{i} with $ currency"):
                assert currency == "$"
            with allure.step(f"test card №{i} with 666-1000 range"):
                assert 666 <= int(price) <= 1000
        driver.quit()

