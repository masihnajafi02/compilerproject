import os
from constants import parse_tree_save_file, syntax_errors_file


def compare():
    root_dir = "D:\\compiler\\p2\\P2_testcases\\"
    index = 1

    for subdir, dirs, files in os.walk(root_dir):
        for _dir in dirs:
            test_case_id = root_dir + "\\" + _dir + "\\"
            input_txt = open(test_case_id + "input.txt", "r").read()
            open("input.txt", "w").write(input_txt)
            os.system('py compiler.py')
            pt = open(test_case_id + parse_tree_save_file, "r").read().strip()
            se = open(test_case_id + syntax_errors_file, "r").read().strip()
            pt_m = open(parse_tree_save_file, "r").read().strip()
            se_m = open(syntax_errors_file, "r").read().strip()
            print(f"{index}:")
            if pt == pt_m and se == se_m:
                print("All True")
            else:
                print(pt == pt_m, "parse tree")
                print(se == se_m, "Syntax Errors")
                print("=========================================")
            index += 1


compare()
