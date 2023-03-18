from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from .models import Riddle, Option
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    #return render(request, "index.html", {"latest_riddles": Riddle.objects.order_by('-pub_date')[:5]})
    return render(request, 'index.html', context)

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def shop(request):
    return render(request, 'shop.html')

def shop_details(request):
    return render(request, 'shop-details.html')

def shopping_cart(request):
    return render(request, 'shopping-cart.html')

def stats(request):
    return render(request, 'stats.html')

def results(request):
    return render(request, 'results.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def answer5(request):
    return render(request, 'answer.html')

def answer0(request):
    return render(request, 'answer0.html')
def answer1(request):
    return render(request, 'answer1.html')
def answer2(request):
    return render(request, 'answer2.html')
def answer3(request):
    return render(request, 'answer3.html')
def answer4(request):
    return render(request, 'answer4.html')


def questionaire(request):
    return render(request, 'questionaire.html')
def questionaire1(request):
    return render(request, 'questionaire1.html')
def questionaire2(request):
    return render(request, 'questionaire2.html')
def questionaire3(request):
    return render(request, 'questionaire3.html')
def questionaire4(request):
    return render(request, 'questionaire4.html')
def questionaire5(request):
    return render(request, 'questionaire5.html')
def answer(request, riddle_id):
    riddle = get_object_or_404(Riddle, pk=riddle_id)
    try:
        option = riddle.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        return render(request, 'answer.html', {'riddle': riddle, 'error_message': 'Option does not exist'})
    else:
        if option.correct:
            return render(request, "index.html", {"latest_riddles": Riddle.objects.order_by('-pub_date')[:5], "message": "Nice! Choose another one!"})
        else:
            return render(request, 'answer.html', {'riddle': riddle, 'error_message': 'Wrong Answer!'})

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
import logging

def results(request, question_id):
    # import logging
    # import logging.config
    # logging.config.fileConfig('logging.conf')
    # logger = logging.getLogger('applog')
    logging.debug("Log message goes here.")
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    # print(question.choice_set.all())
    labels = []
    for choice in question.choice_set.all:
        labels.append(choice.choice_text)
    print(labels)
    return render(request, 'results.html', {'question': question, 'lbls': labels, })
#   def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('riddles:results', args=(question.id,)))