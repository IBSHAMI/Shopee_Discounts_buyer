from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from product_reader import ProductReader


# chrome driver path
chrome_driver_path = r"C:\Users\user\PycharmProjects\Prof_Projects\chromedriver_win32\chromedriver.exe"
service = Service(chrome_driver_path)

# make chrome run in the background without opening a new window each time the program is run
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# create the driver
driver = webdriver.Chrome(service=service, options=options)

# create product reader class
product_page = ProductReader(url="https://shopee.com.my/PUMA-NU-TILITY-Men's-Tee-Basics-i.341487315.12327703115", driver=driver)
product_name, product_rating = product_page.get_products_info()
print(product_name)
print(product_rating)

product_variations = product_page.get_product_varations()
print(product_variations)















