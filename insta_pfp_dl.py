from selenium import webdriver

browser= webdriver.Chrome('C:\\Users\\Aritra Marik\\Downloads\\chromedriver_win32(1)\\chromedriver.exe')

user_h=input("Enter the user handle of the profile : ")

url='https://www.instagram.com/'

#concatenate two strings cause that's how we can visit the desired insta profile
url_p = url + user_h

browser.get(url_p)

try:
	image=browser.find_element_by_xpath('//img[@class="_6q-tv"]')

except: 
	image=browser.find_element_by_xpath('//img[@class="be6sR"]')

img_link=image.get_attribute('src')

path="C:\\Users\\Aritra Marik\\Desktop\\python_learn\\"+user_h+".jpg"

import urllib.request

urllib.request.urlretrieve(img_link,path)

print("The desired image has been downloaded at "+path)

browser.quit()