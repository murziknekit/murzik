def find_letter_o(word):
    number_of_o = 0
    for i in word:
        if i =='o':
            print('we find "o"')
            number_of_o += 1
    if number_of_o == 0:
        print('we dont find')
    else:
        print('o:', number_of_o)

'''
word = 'bacon,beef, chicken'
word2 = input()
print (word + word2)
word2.pop = "удалть"
'''

def delete(word2, num):
    print('delete ', word2[num])
    word2.pop(num)
    print(word2)


def add_element(new_list,element):
    print('added ', element)
    new_list.append(element)
    print(new_list)


word = ['bacon','beef', 'chicken' ] 

delete(word,1)
add_element(word, 'cheese')
