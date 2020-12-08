import random
import string

LETTERS = string.ascii_letters
NUMS = '0123456789'
SPE = '!@#$%'
FINAL = LETTERS + NUMS + SPE

len = int(input("PANJANG PASSWORD: "))
password = "".join(random.sample(FINAL, len))
print(password)
