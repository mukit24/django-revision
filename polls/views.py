from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views.generic import ListView, DetailView
# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')
#     # output = '---'.join([q.question_text for q in latest_question_list])
#     context = {
#         'latest_question_list': latest_question_list,
#     }

#     return render(request,"polls/index.html", context)

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')
    

# def detail(request,question_id):
#     question = get_object_or_404(Question, id=question_id)
#     return render(request, 'polls/detail.html',{'question':question})

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

def vote(request, question_id):
    print(request.POST)
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = Choice.objects.get(id=request.POST['choice'])
    except KeyError:
        return render(request,'polls/detail.html',{'question':question,'error_msg':'Please select a choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class ResultView(DetailView):
    model = Question
    template_name = 'polls/results.html'

