from django.shortcuts import render

# Create your views here.
#
from django.http import HttpRequest
from django.http import HttpResponse


# 用户输入http://127.0.0.1:8000/index/，访问该视图

def index(request):
    # return HttpResponse('ok')
    # 模拟数据查询
    context = {
        'name': '马上双十一，点击有惊喜',
    }
    return render(request, 'project/index.html', context=context)
