# import beautifulsoup4
import requests
from product_reader import ProductReader

# use ProductReader to read the product page of random product from shopee


product_page = ProductReader(url="https://shopee.com.my/-Bundle-of-2-ATTACK-Liquid-Detergent-plus-Softener-(LATS)-3.6kg-i.466573414.10748996792")
soup = product_page.soup

print(soup.text)









