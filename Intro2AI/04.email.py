from os import walk

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

 
def text_parse(text):
    """预处理数据

    Args:
        text (str): 邮件内容
    """
    token_list = text.split()
    return [tok.lower() for tok in token_list if len(tok) > 2]


def create_vocab_list(data_set):
    """去除列表中重复元素，并以列表形式返回
    
    Args:
        data_set (list[str]): 各封邮件的拆分后的词汇列表
    """
    vocab_set = set({})
    for d in data_set:
        vocab_set = vocab_set | set(d)  # 取并集去重

    return list(vocab_set)


def words_to_vec(vocab_list, input_set):
    """统计每一封邮件在单词表中出现的次数，并以列表形式返回
    
    Args:
        vocab_list (list[str]): 经并集去重后的词汇表
        input_set (list[str]): 该封邮件内容的词汇列表
    """
    return_vec = [0] * len(vocab_list)

    for word in input_set:
        if word in vocab_list:
            return_vec[vocab_list.index(word)] += 1

    return return_vec


if __name__ == '__main__':
    """朴素贝叶斯主程序
    """

    doc_list, class_list, x = [], [], []
    _, _, spam_filenames = next(walk('email_dataset/spam'))
    _, _, ham_filenames = next(walk('email_dataset/ham'))

    for filename in spam_filenames:
        # 遍历垃圾邮件
        with open('email_dataset/spam/{}'.format(filename), encoding='ISO-8859-1') as f:
            content = f.read()
        word_list = text_parse(content)
        doc_list.append(word_list)
        class_list.append(1)
    for filename in ham_filenames:
        # 遍历非垃圾邮件
        with open('email_dataset/ham/{}'.format(filename), encoding='ISO-8859-1') as f:
            content = f.read()
        word_list = text_parse(content)
        doc_list.append(word_list)
        class_list.append(0)

    # 将数据向量化
    vocab_list = create_vocab_list(doc_list)

    for word_list in doc_list:
        x.append(words_to_vec(vocab_list, word_list))

    # 分割数据为训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(
        x, class_list, test_size=0.25)
    x_train, x_test, y_train, y_test = np.array(x_train), np.array(x_test),\
        np.array(y_train), np.array(y_test)

    print("x_train:", x_train)
    print("y_train:", y_train)

    # 训练模型
    nb_model = MultinomialNB()
    nb_model.fit(x_train, y_train)

    # 测试模型效果
    y_pred = nb_model.predict(x_test)

    # 输出预测情况
    print("正确值 {}".format(y_test))
    print("预测值 {}".format(y_pred))
    print("准确率 %f%%" % (accuracy_score(y_test, y_pred) * 100))
