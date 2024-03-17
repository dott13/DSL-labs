# Lexer and Scanner

## Overview

&ensp;&ensp;&ensp; The term lexer comes from lexical analysis which, in turn, represents the process of extracting lexical tokens from a string of characters. There are several alternative names for the mechanism called lexer, for example tokenizer or scanner. The lexical analysis is one of the first stages used in a compiler/interpreter when dealing with programming, markup or other types of languages.
&ensp;&ensp;&ensp; The tokens are identified based on some rules of the language and the products that the lexer gives are called lexemes. So basically the lexer is a stream of lexemes. Now in case it is not clear what's the difference between lexemes and tokens, there is a big one. The lexeme is just the byproduct of splitting based on delimiters, for example spaces, but the tokens give names or categories to each lexeme. So the tokens don't retain necessarily the actual value of the lexeme, but rather the type of it and maybe some metadata.

## Objectives:

1. Understand what lexical analysis [1] is.
2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
3. Implement a sample lexer and show how it works.

## Implementation

## Tokenizer:

We created a bunch of tokens in our <b>tokens.py</b> file and then we added a class `Token` for different tokens that we will find with our Lexer.

To actually be able to pick the tokens with our lexer we needed to build patterns of our tokens and their finite values. We made 3 patterns using Regular Expressions(RegEx):

```python
    INTEGER_PATTERN = re.compile(r'\d+')
    FLOAT_PATTERN = re.compile(r'[-+]?([0-9]*(\,|\.)[0-9]+|[0-9]+)')
    WHITESPACE_PATTERN = re.compile(r'\s+')
```

## Lexer Implementation

We created a new pythin class `Lexer` that takles the token recognition. To do that we made one function called `get_next_token`.

In this part of our code we are searching for tokens that were inputed by the user. To do this we use our <b>regular expressions(patterns)</b> that we actually settled on in our <i>tokenizer</i>

To search through and understand if our tokens are floats or actually integers we used this portion of code:

```python
float_match = FLOAT_PATTERN.match(text, self.pos)
        if float_match:
            float_str = float_match.group()
            self.pos = float_match.end()
            if '.' in float_str or ',' in float_str:
                float_str = float_str.replace(',', '.')
                return Token(TOKEN_FLOAT, float(float_str))
            else:
                return Token(TOKEN_INTEGER, int(float_str))
```

There we our float or integer to the float string if we see a <b>dot</b> or a new functionality that I added of my own, with a <b>comma</b>. If there are no commas or dots we just get an <i>integer</i>.

Thats basically it we added aswell a portion that helps us skip any white spaces, we just get those spaces as tokens and skip them like this:

```python

whitespace_match = WHITESPACE_PATTERN.match(text, self.pos)
        if whitespace_match:
            self.pos = whitespace_match.end()
            return self.get_next_token()
```

After that we check it our `main` class to see if our <i>Lexer</i> works properly:

```python
lexer = Lexer('2 + 3 * 4 - (5 / 2.52) * 3,14')
    while True:
        token = lexer.get_next_token()
        if token.type == TOKEN_EOF:
            break
        print(token)
```

### Output:

After we managed to input our data and try it ourselves this is our output:

```
Token(INTEGER, 2)
Token(PLUS, '+')
Token(INTEGER, 3)
Token(MULTIPLY, '*')
Token(INTEGER, 4)
Token(MINUS, '-')
Token(LPAREN, '(')
Token(INTEGER, 5)
Token(DIVIDE, '/')
Token(FLOAT, 2.52)
Token(RPAREN, ')')
Token(MULTIPLY, '*')
Token(FLOAT, 3.14)
```

Basically we got our tokens scanned and analized thats kinda all.

## Conclusions

One of the key challenges we tackled was recognizing numbers, particularly integers and floats. We meticulously crafted our lexer to accommodate various numeric formats, including support for both dot and comma as decimal separators. This ensures that numbers are correctly identified and processed regardless of how they're written. Our implementation carefully handles each token, categorizing them into distinct types such as arithmetic operators, parentheses, or numeric values. This systematic approach forms a solid foundation for subsequent stages in our system's workflow, allowing for accurate interpretation and manipulation of mathematical expressions.
