word = 'hel lo nisdjgo jgsopgjsdopgs gjseopgjsdpog soj sopgs'
word2 = 'world '
print((word + word2)*3)
print(word + '4')

print(len(word))

array = word.split('.')
print(word.split('g'))

print(array[0])

if 'g' in word:
    print('we find "gso')
else:
    print('we dont find')

print(array)
array.append('new word')
print(array)  
array.pop() 
print(array)
array.clear()
print(array)