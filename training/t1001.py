# 与えられた2つのパラメータの合計を2倍したものが60をこえているかどうか
def check_sum_2times_over_60(par1, par2):
    if (par1 + par2) * 2 > 60:
        return print("true")

# 与えられた金額に消費税率8%を含めた値が5000を超えているかどうか
def tax_include(cost):
    if (cost * 1.08 > 5000):
        return print("true")

# 与えられたスコアを80以上なら'A'60以上80未満なら'B'、45以上60未満なら'C',
# 45'未満'は'F'と返す
def judge_rank(score):
    if score >= 80:
        print ("A")
    elif 60 < score  < 80:
        print ("B")
    elif 45 < score < 60:
        print ("C")
    else:
        print("F")


# 与えられた数値の階乗を返す。ただし再帰は使用禁止
def factorial(num):
    tmp = 1
    for i in range(num):
        tmp *= i + 1
    print(tmp)


# 与えられた数値の2の累乗を返す= 再起使用禁止。便利な演算子利用禁止。
def power_of_two(num):
    tmp = 1
    for i in range(num):
        tmp *= 2
    print(tmp)

if __name__== '__main__':
    check_sum_2times_over_60(20, 30)
    tax_include(5000)
    judge_rank(60)
    factorial(4)
    power_of_two(3)