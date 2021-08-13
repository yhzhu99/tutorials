from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice


# Create your views here.

def index(request):
    # 获取最新的投票问题，若没有投票问题则返回404错误
    try:
        question = Question.objects.order_by('-pub_date')[0]
    except Question.DoesNotExist:
        raise Http404('还没有投票问题！')
    # 设定使用上面代码中的question填充模板中的变量question
    context = {'question': question}
    # 使用render函数“填充”模板
    return render(request, 'polls/index.html', context)


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        # 获取被投票的选项
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # 若没有选择任何选项，则返回投票页面，并提示错误
        return render(request, 'polls/index.html', {
            'question': p,
            'error_message': '您还没有选任何选项！',
        })  # 将错误信息填充到模板中的变量error_message
    else:
        # 更改数据库，将被投票选项的投票数加1
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponse('投票成功！')
