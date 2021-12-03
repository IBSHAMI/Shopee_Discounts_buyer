# import libraries required for the reader class
import requests
# import beautiful soup library
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
        driver.get(self.url)
        self.html = driver.page_source
        self.soup = BeautifulSoup(self.html, "html.parser")

