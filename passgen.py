import random 
import string
import re
import array


l = int(input('Enter length: ')) 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
lowchars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
upchars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
specialchars = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
 
# combines all the character arrays above to form one array
biglist = numbers + upchars + lowchars + specialchars

rand_digit = random.choice(numbers)
rand_upper = random.choice(upchars)
rand_lower = random.choice(lowchars)
rand_symbol = random.choice(specialchars)
 
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
for i in range(l - 4):
    temp_pass = temp_pass + random.choice(biglist)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
password=''.join(temp_pass)
print('Password is:',password)

if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()<>=.~]).{8,30})',password))==True):
        print("The password is strong")
elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*()<>=.~]*).{8,30})',password))==True):
        print("The password is weak")
