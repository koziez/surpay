from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question, Vote


def index(request):
    if not request.user.is_authenticated :
        if not request.session.session_key:
            request.session.save()
        session_key = request.session.session_key
        answered_list = list(Vote.objects.all().filter(session_key=session_key).values_list('question_id', flat=True))
        question_list = Question.objects.order_by('-date_made')
        for question in question_list:
            if question.id not in answered_list:
                return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))
        return HttpResponseRedirect(reverse('polls:complete'))
    else :
        latest_question_list = Question.objects.order_by('-date_made')
        context = {'latest_question_list': latest_question_list}
        return render(request, 'polls/index.html', context)

def detail(request, question_id):
    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key
    question = get_object_or_404(Question, pk=question_id)
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    return render(request, 'polls/detail.html', {'question': question, 'session_key':session_key})

def vote(request, question_id):
    if not request.user.is_authenticated :
        if not request.session.session_key:
            request.session.save()
        session_key = request.session.session_key
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            question.votes += 1
            selected_choice.votes += 1
            selected_choice.save()
            question.save()

            choices = list(question.choice_set.all())
            for choice in choices:
                percent = choice.votes*100/question.votes
                choice.percentage = percent
                choice.save()

            v = Vote(session_key=session_key, question=question, choice=selected_choice)
            v.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    votes = Vote.objects.filter(question=question)
    if votes :
        return render(request, 'polls/results.html', {'question': question})
    else :
        return render(request, 'polls/empty.html', {'question': question})

def complete(request):
    return render(request, 'polls/complete.html')
