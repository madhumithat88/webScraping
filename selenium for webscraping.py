#basic web scraping
from selenium import webdriver
url = "https://www.youtube.com/playlist?list=PL_Cqw69_m_yz4JcOfmZb2IDWwIuej1xfN"
browser=webdriver.Chrome()
browser.get(url)
browser.find_element_by_xpath('//*[@id="thumbnail"]').click()

