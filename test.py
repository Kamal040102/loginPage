# import model 

# users = model.retrieveUser()
# print(users)

# import main

# print(main.login())

import datetime
import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
all = lower + upper + num
temp = random.sample(all, 20)
key = ''.join(temp)
print(f"{datetime.datetime.now().strftime('%d%m%Y%H%M%S')}{key}")