"""
Mastermind游戏实现
系统先随机生成四个数字，然后用户输入有效范围内的四个数字，程序对两组数字作对比
如果用户输入的四个数字中，某个数字的位置和大小都正确，那么就算一个黑球
如果数字正确位置不正确，算一个白球；否则，不给球。结果显示有几个黑球几个白球
"""

import random


def check(answer, guess):
    answer_used = [False, False, False, False]
    guess_used = [False, False, False, False]
    black_ball = 0
    white_ball = 0
    if answer == guess:
        black_ball = 4
    else:
        for index, value in enumerate(guess):
            if value == answer[index]:
                answer_used[index] = True
                guess_used[index] = True
                black_ball += 1
        for index_g, value_g in enumerate(guess):
            if answer_used[index_g]:
                continue
            for index_a, value_a in enumerate(answer):
                if guess_used[index_a]:
                    continue
                if value_g == value_a:
                    answer_used[index_g] = True
                    guess_used[index_a] = True
                    white_ball += 1
                    break
    return black_ball, white_ball


if __name__ == '__main__':
    generate_answer = "".join([str(random.randint(0, 9)) for _ in range(4)])
    while 1:
        guess_answer = input("请输入要猜测的四位数字：")
        if len(guess_answer) != 4 or not guess_answer.isdigit():
            print("输入错误,请重新输入！")
        else:
            black, white = check(generate_answer, guess_answer)
            if black == 4:
                print("猜对啦!,答案是：{0}".format(generate_answer))
                break
            else:
                print(black, white)
