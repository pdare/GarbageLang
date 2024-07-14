#include <string>
#include <vector>

enum TokenType
{
    Integer,
    Float,
    Identifier,
    Equals,
    OpenParen,
    CloseParen,
    BinaryOperator,
    Var,
};

struct Token
{
    std::string value;
    TokenType type;
};

std::vector<std::string> splitString(const std::string &sourceCode) {
    std::vector<std::string> words;
    std::string word;

    for (char ch : sourceCode) {
        if (ch != ' ') {
            word += ch;
        } else if (!word.empty()) {
            words.push_back(word);
            word.clear();
        }
    }

    if (!word.empty()) {
        words.push_back(word);
    }

    return words;
}

Token token(std::string value, TokenType tokentype)
{
    return {value, tokentype};
}

long long SHIFT_CURR = 0;
std::string shift(std::vector<std::string> &src)
{
    std::string current = src.front();
    src.erase(src.begin());
    return current;
}

std::vector<Token> tokenize(std::string &sourceCode) {
    std::vector<Token> tokens;
    std::vector<std::string> src = splitString(sourceCode);

    while (!src.empty()) {
        if (src.front() == "(") {
            tokens.push_back(token(shift(src), TokenType::OpenParen));
        } else if (src.front() == ")") {
            tokens.push_back(token(shift(src), TokenType::CloseParen));
        }
    }
    return tokens;
}

