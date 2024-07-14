
import re

def reg_test():
    x = '10'
    y = '10.0'
    z = '10.0.0'

    test_int = '\\d*'
    test_float = '\\d*\\.\\d*'

    print('what is x')
    if re.fullmatch(test_int, x) != None:
        print("it's an int")
    elif re.fullmatch(test_float, x) != None:
        print("it's a float")
    else:
        print("it's not an int or float")

    print('what is y')
    if re.fullmatch(test_int, y) != None:
        print("it's an int")
    elif re.fullmatch(test_float, y) != None:
        print("it's a float")
    else:
        print("it's not an int or float")

    print('what is z')
    if re.fullmatch(test_int, z) != None:
        print("it's an int")
    elif re.fullmatch(test_float, z) != None:
        print("it's a float")
    else:
        print("it's not an int or float")


test_str = 'var x = 5; x = 10.2;'
tokens = []

def find_tokens(str_parse):
    global tokens
    i = 0
    temp_token = []
    for token in str_parse:
        if i == 0:
            temp_token.append(token)
        elif token == ';':
            temp_insert = ''
            for t in temp_token:
                temp_insert = temp_insert + t
            tokens.append(temp_insert)
            tokens.append(token)
            temp_token.clear()
        elif token == '(' or token == ')' or token == ',':
            temp_insert = ''
            for t in temp_token:
                temp_insert = temp_insert + t
            tokens.append(temp_insert)
            tokens.append(token)
            temp_token.clear()
        elif i + 1 < len(str_parse) and (str_parse[i-1] == ' ' or str_parse[i+1] == ' ') and token != ' ':
            temp_token.append(token)
        elif i == len(str_parse) - 1 and token != ' ':
            temp_insert = ''
            temp_token.append(token)
            for t in temp_token:
                temp_insert = temp_insert + t
            tokens.append(temp_insert)
            temp_token.clear()
        elif token != ' ' and token != ';':
            temp_token.append(token)
        elif token == ' ' and i != 0 and str_parse[i-1] != ';':
            temp_insert = ''
            for t in temp_token:
                temp_insert = temp_insert + t
            tokens.append(temp_insert)
            temp_token.clear()

        i = i + 1

def main():
    global test_str
    global tokens

    with open('test.garbl', 'r') as f:
        test_str = f.read()
    char_arr = list(test_str)
    
    find_tokens(char_arr)

    temp_tokens = []
    for token in tokens:
        if re.fullmatch('\\s*', token) == None and token != ' ':
            temp_tokens.append(token.strip())
        else:
            print('whitespace found')
    
    for token in temp_tokens:
        print(token)

if __name__ == '__main__':
    main()