from django.http import HttpResponse
from .models import Pyetje, Progress
import random
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register



def index(request):
    if request.user.is_authenticated:
        questions = Pyetje.objects.all()
        progress_query = Progress.objects.filter(user=request.user)
        questions_html, questions_css, questions_javascript, questions_php = 0 , 0, 0, 0
        progress_html, progress_css, progress_javascript, progress_php = 0 , 0, 0, 0
        for question in questions:
            if question.category.id == 1:
                questions_html +=1
            elif question.category.id == 2:
                questions_css +=1
            elif question.category.id == 3:
                questions_javascript +=1
            elif question.category.id == 4:
                questions_php +=1

        for progress in progress_query:
            if progress.category.id == 1:
                progress_html +=1
            elif progress.category.id == 2:
                progress_css +=1
            elif progress.category.id == 3:
                progress_javascript +=1
            elif progress.category.id == 4:
                progress_php +=1

        progress= {
            'html': 0,
            'css': 0, 
            'javascript': 0,
            'php': 0
        }

        if progress_html != 0 or questions_html != 0:
            progress['html'] = int(progress_html / questions_html * 100)
        if progress_javascript != 0 or questions_javascript != 0:
            progress['javascript'] = int(progress_javascript / questions_javascript * 100)
        if progress_css != 0 or questions_css != 0:
            progress['css'] = int(progress_css / questions_css * 100)
        if progress_php != 0 or questions_php != 0:
            progress['php'] = int(progress_php / questions_php * 100)


        return render(request, "index.html", {"progress": progress})
    else:
        progress= {
            'html': 0,
            'css': 0, 
            'javascript': 0,
            'php': 0
        }
        return render(request, "index.html", {"progress": progress})


def html_test(request, category_id):
    try:
        if request.user.is_authenticated:
            answered = [x.question.id for x in Progress.objects.filter(category__id=category_id, user=request.user)]
            pyetjet = list(Pyetje.objects.filter(category__id=category_id).exclude(id__in=answered))
            print("Pyetjet", pyetjet)
            random_question = random.choice(pyetjet)
            context = {'question': random_question}        
            return render(request, "test.html", context)
        else:

            pyetjet = list(Pyetje.objects.filter(category__id=category_id))
            random_question = random.choice(pyetjet)
            if request.session.get(random_question,0) == 0:
                context = {'question': random_question} 
            else:
                request.session[random_question] = random_question
                pyetjet.remove(random_question)
                random_question = random.choice(pyetjet)
                context = {'question': random_question}
            return render(request, "test.html", context)
    except:
        return render(request, "not_found.html")
    # random_item = random.sample(pyetjet, 1)
    

def test_check(request, question_id, answer):
    # correct_answer = Pyetje.objects.get(id=question_id).correct
    question= Pyetje.objects.get(id=question_id)
    correct_answer = question.correct
    category = question.category.id
    
    if correct_answer == answer:
        if request.user.is_authenticated:
            new_answer = Progress.objects.create(question=question,category=question.category, user=request.user)
            new_answer.save()
            return render(request, 'answer_result.html', {'answer': 'correct', 'category': category})
        else:
            new_answer = Progress.objects.create(question=question,category=question.category)
            new_answer.save()
            return render(request, 'answer_result.html', {'answer': 'correct', 'category': category})

    return render(request, 'answer_result.html', {'answer': 'incorrect','category': category})


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'].lower(),
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                return redirect('index')
            else:
                message = 'Login failed!'
    return render(
        request, 'login.html', context={'form': form, 'message': message})


def sign_up(request):
    if request.method == 'GET':
        form = forms.RegisterForm()
        return render(request, 'register.html', {'form': form})    
   
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def create_question(request):
    form = forms.QuestionForm()
    if request.method == 'POST':
        form = forms.QuestionForm(request.POST)
        if form.is_valid():
            question= form.cleaned_data['question'].strip()
            option1 = form.cleaned_data['option1'].strip()
            option2 = form.cleaned_data['option2'].strip()
            option3 = form.cleaned_data['option3'].strip()
            option4 = form.cleaned_data['option4'].strip()
            correct = form.cleaned_data['correct'].strip()
            category = form.cleaned_data['category']
            new_question = Pyetje.objects.create(question=question,option1=option1,option2=option2,option3=option3,
                                                 option4=option4,correct=correct,category=category, created_by=request.user)
            new_question.save()
            messages.success(request, 'Pyetja u shtua me sukses.')
            return redirect('index')
        else:
            return render(request, 'create_question.html', {'form': form})
    return render(request, 'create_question.html', {'form': form})

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)