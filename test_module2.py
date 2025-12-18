import time

time.sleep(3)
class TestShopping:

    def test_product(self, setup):
        setup.find_element('xpath', "//a[text()='HTC One M9']").click()
        time.sleep(2)
    def test_add_to_cart(self, setup):
        setup.find_element('xpath', "//a[text()='Add to cart']").click()
        time.sleep(1)
        setup.switch_to.alert.accept()
        time.sleep(3)
    def test_go_to_cart(self, setup):
        setup.find_element('xpath', "//a[text()='Cart']").click()
        time.sleep(2)
        setup.implicitly_wait(10)
    def test_checkout(self, setup):
        setup.find_element('xpath', "//button[text()='Place Order']").click()
        time.sleep(2)
    def test_place_order(self, setup):
        setup.find_element('id', 'name').send_keys('Ankesh verma')
        time.sleep(1)
        setup.find_element('id', 'country').send_keys('India')
        time.sleep(1)
        setup.find_element('id', 'city').send_keys('New Delhi')
        time.sleep(1)
        setup.find_element('id', 'card').send_keys('8567-8587-9875-8745')
        time.sleep(1)
        setup.find_element('id', 'month').send_keys('December')
        time.sleep(1)
        setup.find_element('id', 'year').send_keys('2025')
        time.sleep(1)
        setup.implicitly_wait(10)

    def test_purchase_order(self, setup):
        setup.find_element('xpath', "//button[text()='Purchase']").click()
        time.sleep(2)
        setup.implicitly_wait(10)
        setup.find_element('xpath', "//button[text()='OK']").click()
        time.sleep(3)
