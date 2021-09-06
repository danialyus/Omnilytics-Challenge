import random
import string
import os
import time
import sys

#random integer
def integer(int1, int2):
    int_output = random.randint(int1, int2)
    return str(int_output)

#random real number
def realnumber(real1, real2, start, end):
    length = random.randint(start, end)
    real_output = round(random.uniform(real1, real2), length)
    return str(real_output)

#random alphabetical
def alphabetical(alph1, alph2):
    length = random.randint(alph1, alph2)
    alph_output = ''.join(random.choices(string.ascii_letters, k = length))
    return alph_output

#random alphanumeric
def alphanumeric(alnum1, alnum2):
    length = random.randint(alnum1, alnum2)
    alnum_output = ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))
    if alnum_output.isalnum() and not alnum_output.isalpha() and not alnum_output.isnumeric():
        space1 = random.randint(1,10)
        space2 = random.randint(1,10)
        alnum_output = ' '*space1 + alnum_output + ' '*space2
    return alnum_output

#generate random objects
def gen_text(
    int1 = 0,
    int2 = 100000,
    real1 = 0,
    real2 = 10000,
    start = 0,
    end = 10,
    alph1 = 5,
    alph2 = 30,
    alnum1 = 5,
    alnum2 = 30):

    output = ''
    size = sys.getsizeof(output)
    

    while size < 10485760:

        sys.stdout.write(f"\rGenerating output, current size is {size/1000000} MB")
        select = ''
        select += random.choice([
            realnumber(real1,real2,start,end), 
            integer(int1,int2), 
            alphabetical(alph1,alph2), 
            alphanumeric(alnum1,alnum2)])
        
        output += select + ','
        size = sys.getsizeof(output)
    
    output = output.strip(",")
    file = open("Omnilytics.txt","w")
    file.write(output)
    file.close
    sys.stdout.write(f"\nGenerated file size is {size/1000000} MB\n")
    return output

#check object type
def check_type(result):
    if result.strip().isdigit():
        return "integer"
    elif result.strip().isalpha():
        return "alphabetical strings"
    elif result.strip().isalnum():
        return " alphanumeric"
    else:
        return "real numbers"

#read generated file
def read_text():
    if "Omnilytics.txt" in os.listdir():
        file = open("Omnilytics.txt", "r")
        list = file.read()
        index = list.split(",")
        for i in index:
            dtype = check_type(i)
            print(f"{i.strip()} - {dtype}\n")
    
    else:
        print ("File has not been generated or removed. Please generate a new file.\n")

while True:

    number = input("Enter 1 to generate random string, Enter 2 to read generated file, Enter 3 to exit\n")
    if number == "1":
        gen_text()
    elif number == "2":
        read_text()
    elif number == "3":
        exit()
    else:
        print ("Please enter a valid number...\n")