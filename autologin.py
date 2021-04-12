from selenium import webdriver

user_id=input("Enter the email or phone number:")
password=input("Enter the password:")

browser= webdriver.Chrome('C:\\Users\\Aritra Marik\\Downloads\\chromedriver_win32\\chromedriver.exe')
browser.get('https://www.facebook.com/')


element=browser.find_element_by_id("email")
element.send_keys(user_id)
element1=browser.find_element_by_id("pass")
element1.send_keys(password)

login=browser.find_element_by_id("u_0_b")
login.click()

browser.quit()