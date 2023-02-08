"""Scrapes quotes from the given url.

The url is 'https://quotes.toscrape.com/'.
"""

import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

url = 'https://quotes.toscrape.com/'
driver.get(url)

quotes = driver.find_elements('xpath', '//span[@class="text"]')

data = []
for q in quotes:
    data.append(q.text)
    
driver.quit()

df = pd.DataFrame(data, columns=['Quotes'])
st.dataframe(df)
