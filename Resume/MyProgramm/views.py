from django.shortcuts import render, redirect
from .models import Text
from .models import Word
from .models import TextFormat
from .forms import TextForm, WordForm,TextFormatForm
from termcolor import colored


def myprogramm(request):
    form = TextForm()
    formatform = TextFormatForm()
    if request.method == 'POST':
        form = TextForm(request.POST)
        formatform = TextFormatForm(request.POST)
        if form.is_valid() and formatform.is_valid():
            form.save()
            formatform.save()
            return redirect('wordslist')
    data = {
        'form': form,
        'formatform': formatform
    }
    return render(request, 'MyProgramm/myprogramm.html', data)

def WordsList(request):
    text = TextFormat.objects.order_by('-id')[:1] #тут должен быть вывод из таблицы формат. текст со словарем
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result')
    form = WordForm()
    data = {
        'form': form,
        'text': text
    }
    return render(request, 'MyProgramm/wordslist.html', data)

def Result(request):
    text = Text.objects.order_by('-id')[:1]
    data = {
        'text': text
    }
    return render(request, 'MyProgramm/result.html',data)


