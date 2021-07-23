import random

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = upper.lower()
numbers = '0123456789'
symbols = '%$^!()[]*^&@#;,.'
all=lower+upper+numbers+symbols
length=73
password="".join(random.sample(all, length))
print(password)
