import pywhatkit as kit
# 

import time
# import datetime
phone_numbers = ["+923090001571","+923015742263","+923401258104","+923114377657","+923058187111" ] 
message = "hyyy!!"
# now=datetime.datetime.now()
# send_hour=now.hour
# send_min=now.minute+3
for number in phone_numbers:
  kit.sendwhatmsg_instantly(number, message,wait_time=10)
  time.sleep(3)
