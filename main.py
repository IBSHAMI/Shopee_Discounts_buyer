from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from product_reader import ProductReader


# chrome driver path
chrome_driver_path = r"C:\Users\user\PycharmProjects\Prof_Projects\chromedriver_win32\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


product_page = ProductReader(url="https://shopee.com.my/product/26912497/1881778163", driver=driver)
soup = product_page.soup

print(soup)











