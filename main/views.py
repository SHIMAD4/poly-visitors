from django.shortcuts import render
from rest_framework import viewsets

from .models import Statement, Dormitory
from .serializers import StatementSerializer, DormitorySerializer


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def statement_home(request):
    statements = Statement.objects.all()
    return render(request, "main/statements.html", {"statements": statements})


class StatementViewSet(viewsets.ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer


class DormitoryViewSet(viewsets.ModelViewSet):
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer
