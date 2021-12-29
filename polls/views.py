import math

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question
from .forms import ContactForm, QuestionForm, TriangleForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'


    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                from_email='noreply@mysite.com',
                recipient_list=[form.cleaned_data["email"]],
            )
            return redirect('polls:contact_form')
    else:
        form = ContactForm(initial={"email": "test@test.com"})
    return render(request, 'contact_form.html', {
        'form': form,

    })


def create_form(request):
    form = ContactForm(initial={"email": "test@test.com"})
    return render(request, 'contact_form.html', {
        'form': form,

    })


def process_form(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        return redirect('polls:create_form')
    return render(request, 'contact_form.html', {
        'form': form,
    })


def create_question_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # question = Question.objects.create(
            #     question_text=form.cleaned_data.get('question_text'),
            #     pub_date=form.cleaned_data.get('pub_date'),
            # )
            question = form.save(commit=False)
            question.owner = request.owner
            question.save()
            return redirect('polls:detail', pk=question.pk)
    else:
        form = QuestionForm(initial={'pib_date': timezone.now()})
    return render(request, 'create_question_form.html', {
        'form': form,

    })


def triangle_form(request):
    if request.method == 'POST':
        form = TriangleForm(request.POST)
        if form.is_valid():
            hypotenuse = math.sqrt(form.cleaned_data['a'] ** 2 + form.cleaned_data['b'] ** 2)
            return render(request, 'polls/triangle_form.html', {
                'hypotenuse': hypotenuse,
            })
    else:
        form = TriangleForm()
    return render(request, 'polls/triangle_form.html', {
            'form': form,
    })
