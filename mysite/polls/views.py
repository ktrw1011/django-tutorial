from django.http import request
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # templateをロードしてcontextに変数をセットするというのはよく使われるので
    # render()でショートカットできる
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list
    }
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
