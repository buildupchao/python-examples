"""
统计文件中，数字、字母、空格个数
"""

def do_data_type_statistics(filepath):
    num_of_digit = num_of_alpha = num_of_space = 0
    file = open(filepath, 'r')
    for line in file:
        for character in line:
            if character.isdigit():
                num_of_digit += 1
            elif character.isalpha():
                num_of_alpha += 1
            elif character.isspace():
                num_of_space += 1

    file.close()
    return num_of_digit, num_of_alpha, num_of_space


def do_character_statistic(filepath):
    num_of_digit = num_of_alpha = num_of_space = 0
    with open(filepath, 'r') as f:
        for line in f:
            for character in line:
                if character.isdigit():
                    num_of_digit += 1
                elif character.isalpha():
                    num_of_alpha += 1
                elif character.isspace():
                    num_of_space += 1
    return num_of_digit, num_of_alpha, num_of_space


if __name__ == '__main__':
    filepath = '../data/data.txt'
    #total_of_digit, total_of_alpha, total_of_space = do_data_type_statistics(filepath)
    total_of_digit, total_of_alpha, total_of_space = do_character_statistic(filepath)
    print("数字:", total_of_digit)
    print("字母:", total_of_alpha)
    print("空格:", total_of_space)