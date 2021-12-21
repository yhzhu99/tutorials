class Account:
    """账号信息表类

    Args:
        A (float): 日志密度
        B (float): 好友密度
        C (int): 真实头像
        Y (int): 真实账号
    """

    def __init__(self, A, B, C, Y):
        self.A = A
        self.B = B
        self.C = C
        self.Y = Y


# 根据案例对应10个账号信息
a01 = Account(0.05, 0.12, 1, 0)
a02 = Account(0.01, 0.02, 0, 0)
a03 = Account(0.25, 0.58, 0, 1)
a04 = Account(0.15, 0.35, 1, 1)
a05 = Account(0.14, 0.31, 0, 0)
a06 = Account(0.08, 0.18, 0, 0)
a07 = Account(0.09, 0.21, 1, 1)
a08 = Account(0.11, 0.25, 1, 1)
a09 = Account(0.19, 0.44, 1, 1)
a10 = Account(0.21, 0.48, 0, 1)

# 插入到账号list中
account_list = [a01, a02, a03, a04, a05, a06, a07, a08, a09, a10]

# 计算训练样本中总、真实、假账号的个数
tot_cnt = len(account_list) # 总账号数
true_cnt = 0 # 真实账号数
for a in account_list:
    if a.Y == 1:
        true_cnt += 1
false_cnt = tot_cnt - true_cnt # 虚假账号数

p_y_eq1 = true_cnt / tot_cnt  # P(Y=0)
p_y_eq0 = 1 - p_y_eq1  # P(Y=1)
print('P(Y=0):', p_y_eq0, 'P(Y=1):', p_y_eq1)

# 定义各字段划分的界限
bar_a = 0.1
bar_b = 0.3
bar_c = 0

def P(case, cur, y):
    """计算各种情况的概率函数

    Args:
        case (str): 字段类型 A / B / C
        cur (float/int): 当前该字段的值
        y (int): y=1 or y=0 分别对应 P(Y=1) 和 P(Y=0)
    """

    tmp_cnt = 0 # 临时变量，计算符合条件的账号个数
    if case == 'A' and cur > bar_a and y == 0:
        for a in account_list:
            if a.A > bar_a and a.Y == 0:
                tmp_cnt += 1
        return tmp_cnt / false_cnt
    if case == 'A' and cur <= bar_a and y == 0:
        for a in account_list:
            if a.A <= bar_a and a.Y == 0:
                tmp_cnt += 1
        return tmp_cnt / false_cnt
    if case == 'B' and cur > bar_b and y == 0:
        for a in account_list:
            if a.B > bar_b and a.Y == 0:
                tmp_cnt += 1
        return tmp_cnt / false_cnt
    if case == 'B' and cur <= bar_b and y == 0:
        for a in account_list:
            if a.B <= bar_b and a.Y == 0:
                tmp_cnt += 1
        return tmp_cnt / false_cnt
    if case == 'C' and cur == 0 and y == 0:
        for a in account_list:
            if a.C == 0 and a.Y == 0:
                tmp_cnt += 1
        return tmp_cnt / false_cnt
    if case == 'C' and cur == 1 and y == 0:
        for a in account_list:
            if a.C == 1 and a.Y == 0:
                tmp_cnt += 1
        return tmp_cnt / false_cnt
    if case == 'A' and cur > bar_a and y == 1:
        for a in account_list:
            if a.A > bar_a and a.Y == 1:
                tmp_cnt += 1
        return tmp_cnt / true_cnt
    if case == 'A' and cur <= bar_a and y == 1:
        for a in account_list:
            if a.A <= bar_a and a.Y == 1:
                tmp_cnt += 1
        return tmp_cnt / true_cnt
    if case == 'B' and cur > bar_b and y == 1:
        for a in account_list:
            if a.B > bar_b and a.Y == 1:
                tmp_cnt += 1
        return tmp_cnt / true_cnt
    if case == 'B' and cur <= bar_b and y == 1:
        for a in account_list:
            if a.B <= bar_b and a.Y == 1:
                tmp_cnt += 1
        return tmp_cnt / true_cnt
    if case == 'C' and cur == 0 and y == 1:
        for a in account_list:
            if a.C == 0 and a.Y == 1:
                tmp_cnt += 1
        return tmp_cnt / true_cnt
    if case == 'C' and cur == 1 and y == 1:
        for a in account_list:
            if a.C == 1 and a.Y == 1:
                tmp_cnt += 1
        return tmp_cnt / true_cnt


# 创建以下account_test账号，预测该账号是否是真实账号
account_test = Account(0.15, 0.2, 1, None)

# P(Y=1)P(A=0.15,B=0.2,C=1|Y=1)
# = P(Y=1)P(A=0.15|Y=1)P(B=0.2|Y=1)P(C=1|Y=1)
p_test_y_eq1 = p_y_eq1 * P('A', account_test.A, 1) * \
    P('B', account_test.B, 1) * P('C', account_test.C, 1)
# 同理，当P(Y=0)P(A=0.15,B=0.2,C=1|Y=0)时
p_test_y_eq0 = p_y_eq0 * P('A', account_test.A, 0) * \
    P('B', account_test.B, 0) * P('C', account_test.C, 0)
print(p_test_y_eq1, p_test_y_eq0)
"""
即计算得到了:
  P(Y=1)P(A=0.15,B=0.2,C=1|Y=1) = p_test_y_eq1 = 0.1111111111111111
  P(Y=0)P(A=0.15,B=0.2,C=1|Y=0) = p_test_y_eq0 = 0.018750000000000003
"""

# 得出推测结论
if p_test_y_eq1 > p_test_y_eq0:
    print('推测为真实账号')
elif p_test_y_eq1 < p_test_y_eq0:
    print('推测为虚假账号')
else:
    print('推测为真实账号和虚假账号的可能性相同')
