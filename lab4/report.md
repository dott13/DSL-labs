# Report on Regular Expressions and String Generation

## Introduction

Regular expressions (regex) are powerful tools used for pattern matching in strings. They provide a concise and flexible means to search, extract, and manipulate text based on specific patterns. Regular expressions consist of a sequence of characters and special metacharacters that define a search pattern.

## Objectives

1. Write and cover what regular expressions are, what they are used for;

2. Below you will find 3 complex regular expressions per each variant. Take a variant depending on your number in the list of students and do the following:

   a. Write a code that will generate valid combinations of symbols conform given regular expressions (examples will be shown).

   b. In case you have an example, where symbol may be written undefined number of times, take a limit of 5 times (to evade generation of extremely long combinations);

   c. **Bonus point**: write a function that will show sequence of processing regular expression (like, what you do first, second and so on)

Write a good report covering all performed actions and faced difficulties.

## Applications of Regular Expressions

Regular expressions find extensive use in various domains, including:

- Text processing and search operations
- Data validation and input sanitization
- Parsing and extracting information from structured or semi-structured text
- Text transformation and manipulation
- Web scraping and data extraction
- Lexical analysis in programming languages and compilers

## Complex Regular Expressions

Here are three complex regular expressions for each variant:

2. Variant 2:

   - `M?(N){2}(O|P){3}Q*R+`
   - `(X|Y|Z){3}8+(9|0){2}`
   - `(H|i)(J|K)L*N?`

## String Generation Code

Below is the Python code to generate valid combinations of symbols conforming to the given regular expressions. The code also includes a function to show the sequence of processing the regular expression.

This is the generation definition.

```python
generated_strings_list = []
    for regex_list_item in regex_list:
        regex = random.choice(regex_list_item)
        print("Processing regex:", regex)
```

After we defined all these things we do the following:

```python
try:
            # Compile the regular expression pattern
            pattern = re.compile(regex)
            # Initialize an empty set to store already generated strings for this regex
            generated_set = set()
            # Initialize an empty list to store valid strings for this regex
            generated_strings = []
            # Generate strings until we reach the limit
            attempts = 0
            while len(generated_strings) < 3 and attempts < 100:
                generated_string, steps = generate_string(regex)
                # Check if the generated string matches the regular expression and is not already generated
                if pattern.fullmatch(generated_string) and generated_string not in generated_set:
                    generated_set.add(generated_string)
                    generated_strings.append((generated_string, steps))
                attempts += 1
            generated_strings_list.append(generated_strings)
        except re.error:
            print("Invalid regex:", regex)
    return generated_strings_list
```

We do a try for every string we create with our regex to understand if the patarn is right, the generated strings and etc... It will then generate our string by checking with <i>fullmatch</i> function of re module we imported to our project.

As you can see we have a <b>generate_strings</b> function. This is the function we check every part for our string creation, this is to show you the steps to create our strings(<i> bonus point</i>)

```python
def generate_string(regex):
    string = ""
    transitions = []
    i = 0
```

To find a match the easiest way is to compare with every command we include in our regex list, for example in this case it searches for every open paranthesese and closed ones to ensure it finds all the matches needed in the interiour of the parentesese, after that it uses the inbuilt method <i>findall</i> and concats the character gotten to our string working for our transitions part aswell.

```python
    while i < len(regex):
        if regex[i] == "(" and regex.find(")", i) == len(regex) - 1 or (regex[i] == "(" and regex[regex.find(")", i) + 1] not in ["*", "+", "?", "{"]):
            char = random.choice(options(re.findall(r'\((.*?)\)', regex[i:])[0]))
            string += char
            transitions.append((f"{string[-2]} -> {char}" if len(string) >= 2 else f"Start -> {char}"))
            i = regex.find(")", i)
```

We do the same steps every time we find a match to our string to show you how the tokens found by our defined regex are added to our string.

## Conclusion

In this report, we explored the concept of regular expressions (regex) and their applications in text processing and pattern matching. Regular expressions serve as powerful tools for searching, extracting, and manipulating text based on specific patterns, providing a versatile and flexible way to handle textual data.

We discussed various applications of regular expressions across different domains, including text processing, data validation, parsing, web scraping, and lexical analysis. Regular expressions find extensive use in programming tasks where pattern matching and text manipulation are essential.

Additionally, we provided examples of complex regular expressions for three different variants, showcasing the diversity of patterns that can be expressed using regex.

Furthermore, we presented Python code to generate valid combinations of symbols conforming to the given regular expressions. The code includes functionality to ensure that generated strings match the specified regex pattern and are not repeated multiple times. It also offers a function to display the sequence of processing the regular expression, providing insights into the string generation process.

Overall, regular expressions are indispensable tools for handling textual data efficiently and accurately, enabling developers to perform various text processing tasks effectively. Understanding regular expressions and their usage empowers developers to tackle complex text-based challenges with confidence and precision.
