# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import datetime
# numbers=["+923211772435" ]
# message="
#  "
# send_hour=10
# send_min=30
# driver=webdriver.Chrome()
# driver.get("https://web.whatsapp.com/")
# input=("press ENTER after QR scane   ")
# while True:
#     now=datetime.datetime.now()
#     if now.hour==send_hour and now.minute==send_min:
#         break
#     time.sleep(1)

# for number in numbers:
#     driver.get(f"https://web.whatsapp.com/send?phone={number}&text={message}")
#     time.sleep(5)
#     msg_box = driver.find_element(By.XPATH, "//div[@contenteditable='true' and @data-tab]")
#     msg_box.send_keys(Keys.ENTER)
#     time.sleep(2)

# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import datetime

# numbers = ["923211772435"]
# message = "AOA! nawa aaya a sonya!!"

# send_hour = 10
# send_minute = 50

# driver = webdriver.Chrome()
# driver.get("https://web.whatsapp.com/")
# input("Press ENTER after QR scan...")

# # Wait for the exact time
# while True:
#     now = datetime.datetime.now()
#     if now.hour == send_hour and now.minute == send_minute:
#         break
#     time.sleep(1)

# for number in numbers:
#     driver.get(f"https://web.whatsapp.com/send?phone={number}")
#     time.sleep(8)  # Wait for chat to load

#     # Type the message directly
#     msg_box = driver.find_element(By.XPATH, "//div[@contenteditable='true' and @data-tab]")
#     msg_box.send_keys(message)
#     time.sleep(1)

#     msg_box.send_keys(Keys.ENTER)  # Press Enter to send
#     print(f" Message sent to {number}")

# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Numbers & message
# numbers = ["+923211772435"]
# message = "AOA! Nawa aaya a sonya!!"

# # Chrome profile ka path set karo (taaki QR baar-baar scan na karna pade)
# options = webdriver.ChromeOptions()
# options.add_argument(r"--user-data-dir=C:\Users\sarbuland\AppData\Local\Google\Chrome\User Data")
# options.add_argument(r"--profile-directory=Default")  # apna profile

# # Browser open karo
# driver = webdriver.Chrome(options=options)
# driver.get("https://web.whatsapp.com/")
# time.sleep(10)  # login hone ka time

# # Har number ko message bhejo
# for number in numbers:
#     driver.get(f"https://web.whatsapp.com/send?phone={number}")
#     time.sleep(6)  # chat open hone ka wait

#     msg_box = driver.find_element(By.XPATH, "//div[@contenteditable='true' and @data-tab]")
#     msg_box.send_keys(message)
#     time.sleep(1)
#     msg_box.send_keys(Keys.ENTER)

#     print(f" Message sent to {number}")

# time.sleep(5)
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import datetime

# # Numbers list without '+' sign
# numbers = ["923211772435"]
# message = "AOA! nawa aaya a sonya!!"

# # Exact time to send
# send_hour = 11     # 12 AM
# send_minute = 11

# driver = webdriver.Chrome()
# driver.get("https://web.whatsapp.com/")
# input("QR scan karo aur ENTER dabao...")  # Wait for QR scan

# # Wait for exact time
# while True:
#     now = datetime.datetime.now()
#     if now.hour == send_hour and now.minute == send_minute:
#         break
#     time.sleep(1)

# # Send messages
# for number in numbers:
#     driver.get(f"https://web.whatsapp.com/send?phone={number}")
#     time.sleep(8)  # Wait for chat to load

#     msg_box = driver.find_element(By.XPATH, "//div[@contenteditable='true' and @data-tab]")
#     msg_box.send_keys(message)
#     time.sleep(1)
#     msg_box.send_keys(Keys.ENTER)
#     print(f"Message sent to {number}")
#     time.sleep(2)

# driver.quit()
