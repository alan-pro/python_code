from django.db import models

# Create your models here.
""""
模型继承models.Model
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=18)

    # 重写 str方法以让admin显示书籍名称
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
