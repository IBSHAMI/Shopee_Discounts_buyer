# import libraries required for the reader class
import requests
# import beautiful soup library
from bs4 import BeautifulSoup
# import csv library
import csv
from selenium import webdriver



class ProductReader:
    """
    This class is responsible for reading the products from the website page
    """

    def __init__(self, url):
        """
        Initialize the class with the url to get website data
        """
        self.url = url
        driver = webdriver. Chrome()
        driver.get(self.url)
        self.response = driver.page_source
        self.soup = BeautifulSoup(self.response.text, "html.parser")
