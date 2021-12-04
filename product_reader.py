from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class ProductReader:
    """
    This class is responsible for reading the products from the website page
    """

    def __init__(self, url, driver):
        """
        Initialize the class with the url to get website data
        """
        self.url = url
        self.driver = driver
        self.driver.get(self.url)
        self.html = self.driver.page_source

    def get_products_info(self):
        """
        parse the product information from the soup text attribute

        :return:
        product name
        product rating
        """

        # get product name using css selector
        product_name = self.driver.find_element_by_css_selector(".product-briefing .flex span").text

        # get product rating using xpath
        product_xpath = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div['
                                                          '3]/div/div[2]/div[1]/div[1]').text

        return product_name, product_xpath















