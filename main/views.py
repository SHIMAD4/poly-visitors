from django.shortcuts import render

from .models import Statement


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def statement_home(request):
    statements = Statement.objects.all()
    return render(request, "main/statements.html", {"statements": statements})
