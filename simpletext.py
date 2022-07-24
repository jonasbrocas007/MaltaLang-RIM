#simple text compiler from the .bin file
f = open('code.bin', 'r')
loser = f.readlines()
new_loser = ''

#make the null chars disapper and prints the filtered bin file
for char in loser: 
    new_loser += char
print(new_loser)