from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://leonardlabita.com')

elem = browser_element_by_css_selector('html')

elem.text