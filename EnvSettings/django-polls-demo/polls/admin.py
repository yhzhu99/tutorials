from django.contrib import admin
from .models import Question, Choice


# Register your models here.

# admin.site.register(Question)
class ChoiceInline(admin.StackedInline):  # 默认显示3个选项的列表
    model = Choice
    extra = 3

    # 自定义的投票问题表单


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['question_text']
        }
         ),
        ('Date information', {
            'fields': ['pub_date'],
            'classes': ['collapse']
        }
         )
    ]  # 投票问题和发布时间

    inlines = [ChoiceInline]  # 投票问题的选项


admin.site.register(Question, QuestionAdmin)  # 将自定义表单注册到管理页
