
# 画面に自分の「学科名」「学年」「学籍番号」を出力してください
def print_self_information():
    print ("ITスペシャリスト科")
    print ("2年")
    print ("s15011")

# 自分の年齢が、80歳になるまであと何年か計算して出力してください
def print_how_many_yeart_to80():
    print(80-22)

# 与えられた整数パラメータが「偶数」が「奇数」かを出力してください
def print_odd_orever(target):
    if target % 2 == 0:
        print("偶数")
    elif target % 2 == 1:
        print("奇数")

# randomモジュールを使用して0-50の整数を生成し、25が出るまで「ほげ」と出力してください
def print_hoge():
    from random import randint


# 100から1000までの偶数のみ表示してください
def print_even_from_100_to_1000():
    for i in range(100, 1001):
        if i % 2 == 0:
            print(i)

if __name__ == '__main__':
    print_self_information()
    print_how_many_yeart_to80()
    print_odd_orever(10)
    print_odd_orever(13)
    print_hoge()
    print_even_from_100_to_1000()