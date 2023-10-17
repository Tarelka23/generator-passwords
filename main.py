import random

q1 = "1234567890-=_+~qwertyuiop[]asdfghjkl;zxcvbnm,./QWERTYUIOPASDFGHJKL:ZXCVBNM<>"
dlina = int(input('Из скольки символоф вы хотите пароль?:'))
for i in range(10):
    password = ''
    for a in range(dlina):
        password += random.choice(q1)
    print(password)