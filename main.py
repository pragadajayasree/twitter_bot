from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

UP = 150
DOWN = 40
EMAIL = os.environ["TWITTER_EMAIL"]
PASSWORD = os.environ["TWITTER_PASSWORD"]
USERNAME = os.environ["TWITTER_USERNAME"]


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_option)

        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        try:

            self.driver.get(url="https://www.speedtest.net/")
            time.sleep(3)
            accept_btn = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
            accept_btn.click()

            time.sleep(2)

            go_btn = self.driver.find_element(by=By.XPATH,
                                              value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
            go_btn.click()

            time.sleep(50)

            down = self.driver.find_element(by=By.XPATH,
                                            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
            self.down = down.text
            up = self.driver.find_element(by=By.XPATH,
                                          value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
            self.up = up.text
            self.driver.quit()
            print("down=", self.down)
            print("up=", self.up)

        except NoSuchElementException:

            self.driver.quit()
            self.driver = webdriver.Chrome(options=self.chrome_option)
            self.get_internet_speed()

    def tweet_at_provider(self):
        driver1 = webdriver.Chrome(options=self.chrome_option)
        driver1.get(url="https://twitter.com/login")
        time.sleep(5)
        try:
            inp_email = driver1.find_element(by=By.XPATH,
                                             value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
            inp_email.send_keys(EMAIL)
            time.sleep(2)
            next_btn = driver1.find_element(by=By.XPATH,
                                            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
            next_btn.click()
            time.sleep(2)

            user_name = driver1.find_element(by=By.XPATH,
                                             value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            user_name.send_keys(USERNAME)

            next_1 = driver1.find_element(by=By.XPATH,
                                          value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button')
            next_1.click()

            time.sleep(2)

            pass_word = driver1.find_element(by=By.XPATH,
                                             value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            pass_word.send_keys(PASSWORD)
            time.sleep(2)
            login = driver1.find_element(by=By.XPATH,
                                         value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
            login.click()
            time.sleep(3)
            post = driver1.find_element(by=By.XPATH,
                                        value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
            post.click()
            time.sleep(2)
            post_text = driver1.find_element(by=By.XPATH,
                                             value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')
            post_text.send_keys(
                f"hey internet provider, why is my internet speed {self.down}down and {self.up}up when i pay for {DOWN}/{UP}")
            time.sleep(2)
            send = driver1.find_element(by=By.XPATH,
                                        value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]')
            send.click()
            time.sleep(3)
            driver1.quit()

        except NoSuchElementException:
            driver1.quit()
            self.tweet_at_provider()


obj = InternetSpeedTwitterBot()
obj.get_internet_speed()
obj.tweet_at_provider()
