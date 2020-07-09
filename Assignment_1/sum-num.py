import re
sum = 0
fname = input('Enter file name:')
fh = open(fname)
for line in fh:
    line = line.rstrip()
    str = re.findall('[0-9]+',line)
    for word in str:
        num = int(word)
        sum = sum + num
print('The sum of numbers in the sample text is',sum)