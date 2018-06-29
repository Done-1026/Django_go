from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader

from .models import Question,Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list,}
    #output = ','.join([q.question_text for q in latest_question_list])
    #template = loader.get_template('polls/index.html')    #类似于创建一个模板对象   
    #output = template.render(context,request)   #模板载入context，键值对的形式传入，返回一个response
    #return HttpResponse(output)
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    '''
    try:
        question = Question.objects.get(pk=question_id)
        #context = {'question':question}
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html',{'question':question})
    
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
