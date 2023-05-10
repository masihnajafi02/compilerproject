from constants import input_file_name, all_keywords
from helper import is_number, is_letter, is_white_space, is_symbol, is_slash, is_empty, \
    is_invalid_char_after_numbers, is_invalid_char_after_letters
from declarations import Token, TokenType

input_file = open(input_file_name, "r", encoding="UTF-8")
symbol_table = list()
lexical_error = dict()


def insert_kw_to_symbols():
    for keyword in all_keywords:
        symbol_table.append(keyword)


def for_num_token():
    status = read_number()
    return Token(TokenType.NUM, main_read_part, file_line) if status else ""


def for_ws_token():
    global read_line
    read_line = read_line[1:]
    return ""


def for_kw_or_id_token():
    status = read_keyword_or_id()
    if status:
        if main_read_part not in all_keywords and main_read_part not in symbol_table:
            symbol_table.append(main_read_part)
        return Token(TokenType.KEYWORD, main_read_part, file_line) if main_read_part in all_keywords \
            else Token(TokenType.ID, main_read_part, file_line)
    return ""


def for_comment_token():
    go_forward()
    read_comment()
    return ""


def for_sample_token():
    go_forward()
    read_symbol()
    return Token(TokenType.SYMBOL, main_read_part, file_line)


def for_unavailable_token():
    check_shit_chars()
    return ""


def get_next_token():
    global read_line, file_line, main_read_part
    if is_empty(read_line):
        read_line = input_file.readline()
        file_line += 1
    if is_empty(read_line):
        with open('input.txt', 'r') as f:
            hello = f.readlines()
            temp_line_number = len(hello) + 1 if hello[-1].endswith("\n") else len(hello)
        return Token(TokenType.EOF, "$", temp_line_number)
    char_to_check = read_line[0]
    if is_number(char_to_check):
        read_token = for_num_token()
    elif is_white_space(char_to_check):
        read_token = for_ws_token()
    elif is_letter(char_to_check):
        read_token = for_kw_or_id_token()
    elif is_slash(char_to_check):
        read_token = for_comment_token()
    elif is_symbol(char_to_check):
        read_token = for_sample_token()
    else:
        read_token = for_unavailable_token()
    main_read_part = ""
    if read_token != "" and read_token.lexeme != "":
        return read_token
    else:
        return get_next_token()


def go_forward():
    global main_read_part, read_line
    main_read_part = main_read_part + read_line[0]
    read_line = read_line[1:]


def read_all_numbers():
    while read_line != "" and is_number(read_line[0]):
        go_forward()


def read_number():
    read_all_numbers()
    if is_invalid_char_after_numbers(read_line):
        go_forward()
        log_error("Invalid number", file_line)
        return False
    return True


def read_all_letters():
    while read_line != "" and (is_number(read_line[0]) or is_letter(read_line[0])):
        go_forward()


def read_keyword_or_id():
    read_all_letters()
    if is_invalid_char_after_letters(read_line):
        go_forward()
        log_error("Invalid input", file_line)
        return False
    return True


def go_until_star():
    while read_line != "" and read_line[0] != "*":
        go_forward()


def brief_comment(lexeme):
    if len(lexeme) > 7:
        return lexeme[:7] + "..."
    else:
        return lexeme


def comment_close():
    if not is_empty(read_line) and read_line[0] == "*":
        go_forward()
        if not is_empty(read_line) and read_line[0] == "/":
            go_forward()
            return True
    return False


def check_unclosed_comment(line):
    global main_read_part, read_line, file_line
    if is_empty(read_line):
        read_line = input_file.readline()
        file_line += 1
        if is_empty(read_line):
            main_read_part = brief_comment(main_read_part)
            log_error("Unclosed comment", line)
            return True
    return False


def read_comment():
    global main_read_part
    starting_line = file_line
    if not is_empty(read_line) and read_line[0] == '*':
        go_forward()
        while True:
            go_until_star()
            status = comment_close()
            if status:
                return
            status = check_unclosed_comment(starting_line)
            if status:
                return
    elif not is_empty(read_line) and read_line[0] in "~`!@#$%^&_|?":
        check_shit_chars()
    else:
        log_error("Invalid input", file_line)
    main_read_part = ""


def check_shit_chars():
    if not is_empty(read_line) and read_line[0] in "~`!@#$%^&_|?":
        go_forward()
        log_error("Invalid input", file_line)


def check_equality_and_assign():
    if not is_empty(read_line) and read_line[0] == "=":
        go_forward()
    check_shit_chars()


def check_unmatched_comment():
    if not is_empty(read_line) and read_line[0] == "/":
        go_forward()
        log_error("Unmatched comment", file_line)
    check_shit_chars()


def read_symbol():
    if main_read_part == "=":
        check_equality_and_assign()
    elif main_read_part == "*":
        check_unmatched_comment()


def log_error(error_type, line_num):
    global main_read_part
    if line_num not in lexical_error.keys():
        lexical_error[line_num] = []
    lexical_error[line_num].append((main_read_part, error_type))
    main_read_part = ""


main_read_part = ""
read_line = ""
file_line = 0
