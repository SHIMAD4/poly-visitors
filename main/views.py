from django.shortcuts import render
from rest_framework import generics

from .models import Statement, Dormitory
from .serializers import StatementSerializer, DormitorySerializer


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def statement_home(request):
    statements = Statement.objects.all()
    return render(request, "main/statements.html", {"statements": statements})


class StatementApiView(generics.ListAPIView):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer


class DormitoryApiView(generics.ListAPIView):
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer
