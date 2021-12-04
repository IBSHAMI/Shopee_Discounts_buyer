from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


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

    def get_product_varations(self):
        """
        parse the product variations from the page source text
        :return:
        product variations
        """

        # get hold of the product variations div
        product_info_div = self.driver.find_element_by_css_selector(".product-briefing .flex .flex-auto")

        # transfer the div inner HTML to a soup object
        soup = BeautifulSoup(product_info_div.get_attribute('innerHTML'), 'html.parser')

        # get hold of the third div in the product variations div
        product_variations = soup.find(name="div", class_="_2nr4HE")
        product_variations = product_variations.find_all(name="button", class_="product-variation")

        # get text from each product variation
        product_variations_text = []
        for product_variation in product_variations:
            # get class attribute
            product_variation_class = product_variation.get('class')

            # check if product variation still able to be selected
            disabled_variation_check = [False if "disabled" in x else True for x in product_variation_class]

            # only get the variations if it is still able to be selected
            if all(disabled_variation_check):
                # get text from the product variation
                product_variation_text = product_variation.text
                product_variations_text.append(product_variation_text)

        return product_variations_text
