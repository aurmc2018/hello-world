char_set1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789012!@#$%^&*()_+"
char_set = "01010101010101010101010101010101010101010101010101010101010101010101010101010"

length = len(char_set)
line=""
for i in range(1,76):
        line += '-'
print(line)
i=1
while True:
   for i in range(1,76):
        print(char_set[i:]+char_set[-i:-1])
