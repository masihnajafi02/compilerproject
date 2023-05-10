import re


def is_white_space(char):
    return re.fullmatch("\s", char) is not None


def is_symbol(char):
    return char in ";:,[](){}+-*=<"


def is_slash(char):
    return char == '/'


def is_empty(buffer):
    return buffer == ""


def is_number(char):
    return char in "0123456789"


def is_invalid_char_after_numbers(buffer):
    return not is_empty(buffer) and not is_symbol(buffer[0]) and not is_white_space(buffer[0]) \
           and not is_slash(buffer[0])


def is_letter(char):
    return char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_invalid_char_after_letters(buffer):
    return not is_empty(buffer) and not is_symbol(buffer[0]) and not is_white_space(buffer[0]) \
           and not is_slash(buffer[0])


def write_symbol_table(symbol_table, symbol_table_file):
    counter = 0
    for symbol in symbol_table:
        counter += 1
        symbol_table_file.write(f"{counter}.\t{symbol}\n")


def write_tokens(tokens_list, token_file_name):
    tokens_file = open(token_file_name, "w")
    for index, token_line in tokens_list.items():
        tokens_file.write(f"{index + 1}.\t")
        for token in token_line:
            tokens_file.write(f"({token[0]}, {token[1]}) ")
        tokens_file.write("\n")


def write_lexical_errors(lexical_error, lexical_error_file):
    if len(lexical_error) == 0:
        lexical_error_file.write("There is no lexical error.")
    else:
        for key in sorted(lexical_error.keys()):
            lexical_error_file.write(f"{key}.\t")
            for error in lexical_error[key]:
                lexical_error_file.write(f"({error[0]}, {error[1]}) ")
            lexical_error_file.write("\n")
