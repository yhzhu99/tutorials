import argparse


# step 1. 全局变量初始化
S = None  # 银行存款是否充足 yes / no (type: str)
I = None  # 家庭收入是否充足 yes / no (type: str)
INVESTMENT = None  # 资金使用策略： savings / stocks / combination (type: str)
deposit = None  # 家庭当前银行存款总额 (int)
people = None  # 赡养人数 (type: int)
income = None  # 家庭当前总收入 (type: int)
status = None  # 家庭当前总收入是否是稳定收入，steady / unsteady (type: str)

# step 2. 定义过程中需要用到的几个函数
def mS(y):
    """
    确定最小足够存款额，变元y为家庭赡养人数
    """
    return 5000 * y


def minI(x):
    """
    用于计算当家庭赡养人数为x时，家庭的最小足够收入
    """
    return 50000 + 4000 * x


def GREATER(a, b):
    return a > b


def SUM(x):
    """
    家庭当前银行存款总额
    """
    global deposit
    deposit = x
    return True


def D(x):
    """
    赡养人数
    """
    global people
    people = x
    return True


def E(x, y):
    """
    E表示家庭当前总收入为x，y表示x是否为稳定收入，y只能取steady或unsteady
    """
    global income, status
    income = x
    status = y
    return True

# step 3. 定义规则，即问题领域
def rule01():
    global S, I, INVESTMENT, deposit, people, income, status
    if S == 'no':
        INVESTMENT = 'savings'


def rule02():
    global S, I, INVESTMENT, deposit, people, income, status
    if S == 'yes' and I == 'yes':
        INVESTMENT = 'stocks'


def rule03():
    global S, I, INVESTMENT, deposit, people, income, status
    if S == 'yes' and I == 'no':
        INVESTMENT = 'combination'


def rule04():
    global S, I, INVESTMENT, deposit, people, income, status
    x = deposit
    y = people
    if x is None or y is None:
        return
    if SUM(x) and D(y) and GREATER(x, mS(y)):
        S = 'yes'


def rule05():
    global S, I, INVESTMENT, deposit, people, income, status
    x = deposit
    y = people
    if x is None or y is None:
        return
    if SUM(x) and D(y) and not GREATER(x, mS(y)):
        S = 'no'


def rule06():
    global S, I, INVESTMENT, deposit, people, income, status
    x = income
    y = people
    if x is None or y is None:
        return
    if status == 'steady' and D(y) and GREATER(x, minI(y)):
        I = 'yes'


def rule07():
    global S, I, INVESTMENT, deposit, people, income, status
    x = income
    y = people
    if x is None or y is None:
        return
    if status == 'steady' and D(y) and not GREATER(x, minI(y)):
        I = 'no'


def rule08():
    global S, I, INVESTMENT, deposit, people, income, status
    if status == 'unsteady':
        I = 'no'

# step 4. 推理规则
if __name__ == '__main__':
    help_msg="""
    家庭财务分配管理系统\n
      （用法示例: python main.py --deposit=22000 --income=25000 --steady=True --people=3）
    """
    parser = argparse.ArgumentParser(description=help_msg)
    parser.add_argument('--deposit', required=True, type=int, default=22000, help='请输入家庭当前银行存款总额')
    parser.add_argument('--income', required=True, type=int, default=25000, help='请输入家庭当前总收入')
    parser.add_argument('--steady', required=True, type=bool, default=True, help='是否为稳定输入？True / False')
    parser.add_argument('--people', required=True, type=int, default=3, help='请输入家庭赡养人数')
    
    args = parser.parse_args()
    deposit = args.deposit
    income = args.income
    status = 'steady' if args.steady==True else 'unsteady'
    people = args.people

    while INVESTMENT is None:
        # 反复应用上述规则，直至推导出投资策略
        rule01()
        rule02()
        rule03()
        rule04()
        rule05()
        rule06()
        rule07()
        rule08()
    print(INVESTMENT)  # combination
