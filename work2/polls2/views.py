from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
from django.views import View
from .forms import ContactForm 

"""
#THIS IS FUNCTION BASE VIEW FOR REFFER
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list,}
    return render(request,'polls2/index.html', context)
"""

#THIS IS CLASS BASE VIEW
class index(View):
  def get(self,request):
   latest_question_list = Question.objects.order_by('-pub_date')[:5]
   form =ContactForm()
   context = {'latest_question_list': latest_question_list, 'form': form}
   return render(request,'polls2/index.html', context)

    

  def post(self,request):
    form =ContactForm(request.POST)
    if form.is_valid():
    # form.save() when you make form through model and save this in database
     print(form.cleaned_data['name'])
     return HttpResponse('thanks')  
 
"""def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls2/detail.html', {'question': question})
"""
class detail(View):
  def get(self,request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls2/detail.html', {'question': question})
   

"""def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls2/results.html', {'question': question})
""" 
class results(View):
  def get(self,request,question_id):  
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls2/results.html', {'question': question})


"""
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls2/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
  """
        
class vote(View):
  def post(self,request,question_id): 
   question = get_object_or_404(Question, pk=question_id)
   try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
   except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls2/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
   else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,))) 


class contact(View):
  def get(self,request) :
    form =ContactForm()
    return render(request,'polls2/index.html', {'form':form})
  

  def post(self,request):
    form =ContactForm(request.POST)
    if form.is_valid():
     print(form.cleaned_data['name'])
     return HttpResponse('thanks')  
