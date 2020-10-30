"""
Python作业日期：2020.10.25~2020.10.31 00:00:00
系统初始化为用户生成初始密码，生成的密码要求是随机生成的，并且生成的密码包含一串字符，其中一位数字和一位特殊字符。
要求：
1、可以只传一个参数（即密码长度），可以传递两个参数（用户名，密码长度），也可以传递多个（一组用户名，密码长度）
2、提交py文件、Word、PDF 、jpynb 都可以
"""

import random

"""
@author zhangyachao
@studentNo 2001220198
@date 10/25/2020
"""

# global variable, seeds used for generating password
# consists of 13 special letters, 26 English letters
special_letters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', ';', '?']
special_letters_range = len(special_letters) - 1

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_range = len(letters) - 1

#
# program logic control center
#


def control_center():
    while True:
        print("System will generate password for you, you can choice 3 modes:")
        print("1.only enter the length of password you expect")
        print("2.offer username, the length of password you expect")
        print("3.offer username list, the length of password you expect")

        do_biz_logic()

        to_be_continue = input("Do U wanna continue generating password (N means stopping)?")
        if to_be_continue == "N":
            break
        print("-------------------------------------------------------")

#
# business logic workflow
#


def do_biz_logic():
    choice_mode = 0
    while True:
        choice_mode = input("Please choose mode number:")

        if choice_mode in ("1", "2", "3"):
            break
        else:
            print("error choose mode number, choose again!")

    (username_list, password_lena) = enter_info(choice_mode)

    # start to generate password
    print("The system is generating password, please waiting...")
    user_password_list = generate_password(username_list, password_lena)

    # print password
    print_password(user_password_list)

#
# get username and the length of password from input device
#


def enter_info(choice_mode):

    username_list = []

    if choice_mode == "1":
        pass
    elif choice_mode == "2":
        while True:
            username = input("Please enter username:")
            if len(username):
                username_list.append(username)
                break
            else:
                print("username is invalid, please enter again!")
    else:
        while True:
            username_str = input("Please enter username list with separator comma:")
            if len(username_str) == 0 or username_str == ",":
                print("username list is invalid, please enter again!")
            else:
                username_list = username_str.split(",")
                break

    password_lena = 8
    while True:
        try:
            password_lena = int(input("Please enter the length of password you expect(8~16):"))

            if 8 <= password_lena <= 16:
                break
            else:
                raise ValueError("invalid!!!")
        except:
            print("Invalid!!! The length of password must be integers between 8 and 16! Enter again!")

    return username_list, password_lena

#
# generate init password of user
#


def generate_password(username_list, password_lena):
    user_password_list = []

    if username_list:
        for username in username_list:
            user_password_list.append((username, generate_password_tool(password_lena)))
    else:
        password = generate_password_tool(password_lena)
        user_password_list.append((None, password))

    return user_password_list


def generate_password_tool(password_lena):
    num_of_letters = password_lena - 2

    password_str_list = []
    password_str_list.append(str(random.randint(0, 9)))
    password_str_list.append(special_letters[random.randint(0, special_letters_range)])
    for i in range(0, num_of_letters):
        if i < 3:
            password_str_list.append(letters[random.randint(0, special_letters_range)].upper())
        else:
            password_str_list.append(letters[random.randint(0, special_letters_range)])

    random.shuffle(password_str_list)
    return "".join(password_str_list)

#
# output to console
#


def print_password(user_password_list):
    if user_password_list is None:
        return

    for user_password in user_password_list:
        if user_password[0] is None:
            print("Your password is '%s'." % user_password[1])
        else:
            print("The password of '%s' is '%s'." % (user_password[0], user_password[1]))

if __name__ == '__main__':
    control_center()