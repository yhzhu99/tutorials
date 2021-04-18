from django.db import models  # 引入 Django 中负责模型的模块


class Question(models.Model):  # 自定义模型类需继承models.Model类
    # 定义模型的数据结构
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 定义该对象实例的字符串表示
    def __str__(self):
        return self.question_text


class Choice(models.Model):  # 自定义模型类需继承models.Model类
    # 定义模型的数据结构
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 外键关联
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
