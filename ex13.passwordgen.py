import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','+']


print("Welcome to my password generator")
nr_letters = int(input("How many letters "))
nr_symbols = int(input("How many symbols "))
nr_numbers = int(input("How many numbers "))

#easy Pwd
password=""

for char in range(1, nr_letters +1):
    password += random.choice(letters)

for char in range(1, nr_symbols +1):
    password += random.choice(symbols)

for char in range(1, nr_numbers +1):
    password += random.choice(numbers)

print(f"Easy Password {password}")
#hard pwd
print("-------------------------------------")
pwd=[]
for char in range(1, nr_letters +1):
    pwd += random.choice(letters)

for char in range(1, nr_symbols +1):
    pwd += random.choice(symbols)

for char in range(1, nr_numbers +1):
    pwd += random.choice(numbers)

#reorder list
print(f"Hard pwd b4 shuffle {pwd}")
random.shuffle(pwd)
print(f"Hard pwd after shuffle {pwd}")

pwdd=""

for char in pwd:
 pwdd += char
print("-------------------------------")
print(f"Final password {pwdd}")