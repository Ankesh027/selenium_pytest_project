import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestLogin:
    def test_login(self, setup):
        setup.find_element('xpath', "//span[text()='Login']").click()
        time.sleep(2)
        setup.find_element('xpath', "//input[@class='c3Bd2c yXUQVt']").send_keys("8210676930")
        setup.find_element('xpath', "//button[text()='Request OTP']").click()
        time.sleep(8)

    def test_shopping(self, setup):
        setup.find_element('name',"q").send_keys("Iphone17")
        ac_obj = ActionChains(setup)
        iphone_17 = setup.find_element('xpath',"//li[@class='Sc1DCn']//div[text()='iphone 17 pro']")
        ac_obj.move_to_element(iphone_17).click().perform()
        print("Successfully hovered over iPhone 17")
        time.sleep(2)

        iphone=setup.find_element('xpath','//div[text()="Apple iPhone 17 Pro Max (Deep Blue, 512 GB)"]')
        ac_obj.scroll_to_element(iphone).perform()
        time.sleep(2)
        iphone.click()

        parent_tab = setup.current_window_handle
        setup.find_element('xpath', '//div[text()="Apple iPhone 17 Pro Max (Deep Blue, 512 GB)"]')
        WebDriverWait(setup, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        setup.switch_to.window(setup.window_handles[1])
        print(setup.title)

    def test_add_cart(self, setup):
        setup.find_element('xpath', '//button[@class="dSM5Ub ugg2XR IUmgrZ"]').click() #add to cart
        setup.find_element('xpath', '//button[@class="dSM5Ub JMrpad KcXDCU"]').click()  #place order
        setup.find_element('xpath','//button[@class="dSM5Ub gRSEA4 KcXDCU"]').click()   #select address

    def test_payment(self, setup):

        setup.find_element('xpath','//button[@class="dSM5Ub tzUB8K KcXDCU"]').click()  #c
        setup.find_element('xpath', '//button[@class="dSM5Ub ZjNM9b KtnAdx"]').click()
        setup.find_element('xpath','//button[@class="Button-module_button__P7hTI font-m-semibold Button-module_neutral__OtiH- _8ZaZsG"]').click()


