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

time.sleep(10)

k = '//*[@id="home_birthdays"]/div/div/div/div/a/div/div/span/span[2]'
n = browser.find_element_by_xpath(k).get_attribute('text Content')
num = n[0]
num = int(num)
num = num + 1

mssg= "Happy Birthday !!"
browser.get('https://www.facebook.com/events/birthdays/')

bday_list=browser.find_element_by_xpath("//*[@class='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextArea textInput']")

i=0
for elmnt in bday_list:
	elmnt_id= str(elmnt.get_attribute('id'))
	XPATH= '//*[@id="' + elmnt_id + '"]'
	post= browser.find_element_by_xpath(XPATH)
	#to fetch the box
	post.send_keys(message)#to enter the birthday wish
	post.send_keys(Keys.RETURN)#to send the message
	i = i+1
	if(i>=num):
		break

browser.quit()
