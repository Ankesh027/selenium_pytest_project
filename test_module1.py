import time

class TestSignup:
    def test_signup(self, setup):
        setup.find_element('id', 'signin2').click()
        time.sleep(2)
    def test_username(self, setup):
        setup.find_element('id', 'sign-username').send_keys('Ankesh121@gmail.com')
        time.sleep(2)
    def test_password(self, setup):
        setup.find_element('id', 'sign-password').send_keys('Ankesh@4322')
        time.sleep(2)
    def test_click_signup(self, setup):
        setup.find_element('xpath', "//button[text()='Sign up']").click()
        time.sleep(2)


class TestLogin:

    def test_login(self, setup):
        setup.find_element('xpath', "//a[@id='login2']").click()
        time.sleep(2)
        setup.find_element('id', 'loginusername').send_keys('Ankesh121@gmail.com')
        time.sleep(2)
        setup.find_element('id', 'loginpassword').send_keys('Ankesh@4322')
        time.sleep(2)
        setup.find_element('xpath', "//button[text()='Log in']").click()
        time.sleep(2)
