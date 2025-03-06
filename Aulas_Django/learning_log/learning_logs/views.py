from django.shortcuts import render

# Create your views here.

def index(request):
    """Pagina principal do Learnig_Log"""
    return render(request, 'learning_logs/index.html')