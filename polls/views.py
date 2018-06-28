from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ','.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')    #类似于创建一个模板对象
    context = {
        'latest_question_list':latest_question_list,
        }
    output = template.render(context,request)   #模板载入context，键值对的形式传入，返回一个response
    return HttpResponse(output)

def detail(request, question_id):
    if question_id < 10:
        return HttpResponse("You're looking at question %s." % question_id)
    else:
        raise Http404

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
