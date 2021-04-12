from selenium import webdriver
import time

browser= webdriver.Chrome('C:\\Users\\Aritra Marik\\Downloads\\chromedriver_win32\\chromedriver.exe')
browser.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fext_vrnc%3Dhi%26tag%3Dgooghydrabk-21%26ascsubtag%3D_k_Cj0KCQjwhIP6BRCMARIsALu9Lfng5pIL-7hAhIaj9qwflY38b11R_4u6Td0T9WleSdpsMy5P2BLo1EoaApO3EALw_wcB_k_%26ext_vrnc%3Dhi%26gclid%3DCj0KCQjwhIP6BRCMARIsALu9Lfng5pIL-7hAhIaj9qwflY38b11R_4u6Td0T9WleSdpsMy5P2BLo1EoaApO3EALw_wcB%26ref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

user_id=input("Enter phone number : ")
times=input("Enter number of mssgs : ")

#finding the input number element
element=browser.find_element_by_id("ap_email")
element.send_keys(user_id)

element1=browser.find_element_by_id("continue")
element1.click()

sendOTP=browser.find_element_by_id("continue")
sendOTP.click()


times=int(times)
n=times-1
for i in range(n):
	resend=browser.find_element_by_link_text("Resend OTP")
	resend.click()
	time.sleep(10)

browser.quit()

