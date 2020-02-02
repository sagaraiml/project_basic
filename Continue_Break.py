''' #continue to run the loop
name = ''
while name != 'your name' :
    name = input ('plese enter your name ')
    continue
'''

''' #continue to skip printing
i=0
for i in range(5):  
    if i == 3 :
        continue
    print('inspire yourself times {}'. format (i))
'''

statement = 'I love my India'
for word in statement :
    if word == 'l':
        print('you love somene')
        break
    else:
        print(word)
print('done')
