from django.shortcuts import render
from .models import Topic
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    """Pagina principal do Learnig_Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Mostra um unico assunto e todas as suas entradas"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Adiciona um novo assunto"""
    if request.method != 'POST':
        #Nenhum dado postado entao cria um formulario em branco
        form = TopicForm()
    else:
        #Dado postado entao processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Adiciona uma nova entrada para um assunto especifico"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #Nenhum dado postado entao cria um formulario em branco
        form = EntryForm()
    else:
        #Dado postado entao processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
    