token_list_src = ''
token_types = []

with open('TokenTypes.txt', 'r') as token_file:
    token_list_src = token_file.read()

token_list_src = token_list_src.replace(' ', '')
token_list_src = token_list_src.replace('\n', '')
token_list_src = token_list_src.lstrip(',').rstrip(',')
print(token_list_src)
token_types = token_list_src.split(',')

iterator = 0
for token in token_types:
    print(token)
    if iterator + 1 < len(token_types):
        token_types[iterator] = token + ' = ' + str(iterator) + ','
    else:
        token_types[iterator] = token + ' = ' + str(iterator)
    iterator += 1

f = open('TokenListFinal.txt', 'w')
for token in token_types:
    f.write(token + '\n')
f.close()