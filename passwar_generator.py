import random
import array
MAX_LEN = 12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LCHAR = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 
          			'k', 'm', 'n', 'o', 'p', 'q','r', 's',
             		't', 'u', 'v', 'w', 'x', 'y','z']

UCHAR = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
          			'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
             		'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']

COM_LIST = DIGITS + UCHAR + LCHAR + SYMBOLS
rdigit = random.choice(DIGITS)
rupper = random.choice(UCHAR)
rlower = random.choice(LCHAR)
rsymbol = random.choice(SYMBOLS)
temp = rdigit + rupper + rlower + rsymbol

for x in range(MAX_LEN - 4):
	temp = temp + random.choice(COM_LIST)
	templist = array.array('u', temp)
	random.shuffle(templist)

password = ""
for x in templist:
		password = password + x
		
print(password)
