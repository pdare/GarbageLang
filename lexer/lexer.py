from enum import Enum
import re

class TokenType(Enum):
    Empty = 0,
    Identifier = 1,
    Var_Keyword = 2,
    Func_Keyword = 3,
    Return_Keyword = 4,
    If_Keyword = 5,
    Add_Operator = 6,
    Subtract_Operator = 7,
    Multiply_Operator = 8,
    Divide_Operator = 9,
    Equal_Operator = 10,
    Equality_Operator = 11,
    Open_Paren = 12,
    Close_Paren = 13,
    Open_Bracket = 14,
    Close_Bracket = 15,
    Integer = 16,
    Float = 17,
    Function = 18,
    Statement_Terminator = 19

class Token():
    def __init__(self, t_type, value):
        self.t_type = t_type
        self.value = value

tokens = []
source_code = ''
src_as_char_arr = []
tokens_final = []

# ------- Regex Expressions --------------------------------
test_int = '\\d*'
test_float = '\\d*\\.\\d*'
#-----------------------------------------------------------

keywords = [
    'func',
    'var',
    'return',
    'if'
]

binary_operators = [
    '+',
    '-',
    '*',
    '/'
]

def readSource(file_path):
    global source_code
    global src_as_char_arr
    with open(file_path, 'r') as file:
        source_code = file.read()
    src_as_char_arr = list(source_code)

def find_tokens(str_parse):
    global tokens
    i = 0
    temp_token = []
    tokens_inc_ws = []
    for token in str_parse:
        if i == 0:
            temp_token.append(token)
        elif token == ';':
            temp_insert = ''
            for t in temp_token:
                temp_insert = temp_insert + t
            tokens_inc_ws.append(temp_insert)
            tokens_inc_ws.append(token)
            temp_token.clear()
        elif token == '(' or token == ')' or token == ',':
            temp_insert = ''
            for t in temp_token:
                temp_insert = temp_insert + t
            tokens_inc_ws.append(temp_insert)
            tokens_inc_ws.append(token)
            temp_token.clear()
        elif i + 1 < len(str_parse) and (str_parse[i-1] == ' ' or str_parse[i+1] == ' ') and token != ' ':
            temp_token.append(token)
        elif i == len(str_parse) - 1 and token != ' ':
            temp_insert = ''
            temp_token.append(token)
            for t in temp_token:
                temp_insert = temp_insert + t
            tokens_inc_ws.append(temp_insert)
            temp_token.clear()
        elif token != ' ' and token != ';':
            temp_token.append(token)
        elif token == ' ' and i != 0 and str_parse[i-1] != ';':
            temp_insert = ''
            for t in temp_token:
                temp_insert = temp_insert + t
            tokens_inc_ws.append(temp_insert)
            temp_token.clear()

        i = i + 1
    
    for token in tokens_inc_ws:
        if re.fullmatch('\\s*', token) == None and token != ' ':
            tokens.append(token.strip())
    
    for token in tokens:
        tokens_final.append(Token(findType(token), token))
    for tokes in tokens_final:
        print("{type}: {value}".format(type = tokes.t_type, value = tokes.value))

def findType(t_type):
    if t_type in keywords:
        match t_type:
            case 'var': return TokenType.Var_Keyword
            case 'func': return TokenType.Func_Keyword
            case 'return': return TokenType.Return_Keyword
            case 'if': return TokenType.If_Keyword
            case _: return TokenType.Empty
    elif t_type in binary_operators:
        match t_type:
            case '+': return TokenType.Add_Operator
            case '-': return TokenType.Subtract_Operator
            case '*': return TokenType.Multiply_Operator
            case '/': return TokenType.Divide_Operator
            case _: return TokenType.Empty
    elif t_type == '=':
        return TokenType.Equal_Operator
    elif re.fullmatch(test_float, t_type) != None:
        return TokenType.Float
    elif re.fullmatch(test_int, t_type) != None:
        return TokenType.Integer
    elif t_type == '==':
        return TokenType.Equality_Operator
    elif t_type == '(':
        return TokenType.Open_Paren
    elif t_type == ')':
        return TokenType.Close_Paren
    elif t_type == '{':
        return TokenType.Open_Bracket
    elif t_type == '}':
        return TokenType.Close_Bracket
    elif t_type == ';':
        return TokenType.Statement_Terminator
    else:
        return TokenType.Identifier

def splitString(sc):
    global src_as_char_arr

    i = 0
    for char in src_as_char_arr:
        pass
    '''
    words = sc.split(' ')
    for word in words:
        tokens.append(Token(findType(word), word))
    for tokes in tokens:
        print("{type}: {value}".format(type = tokes.t_type, value = tokes.value))
    '''

def main():
    global src_as_char_arr
    readSource('test.garbl')
    find_tokens(src_as_char_arr)

if __name__ == '__main__':
    main()

'''
source_code = source_code.split(';')
    for line in source_code:
        print(line)
'''