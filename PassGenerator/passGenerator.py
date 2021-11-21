import random

string = 'qQwWeErRtTyYuUiIoOpPAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm'#MAKE A STRING OF ALPHABET
pass_len = input("hi again \nim here to generat password for you\nplz enter the lengh of password you want :\n")#EXPLANE HERE AND ASK ABOUT LENGH OF PASSWORD
password = ''#MAKE PASSWORD TO CREAT PASSWORD
let = input("ok , your password could incloud numbers?(y/n): ")#TAKE LET TO APPEND NUMBERS TO STRING
if let:
    string += '1234567890'#ADD NUMBERS
let = input("and , your password could incloud !@#... ?(y/n): ")#TAKE LET TO APPEND !@#.. TO STRING
if let:
    string += '!@#$%^&*()_+-=}[{]|/?.>,<`~\'"'#ADD THIS TO STRING
for i in range(int(pass_len)):
    password += string[random.randint(1,len(string))]#MAKE PASSWORD WITH CHOOSE RANDOMLY FROM STRING

print(password)#DA DA DA DAAAAAAA
