from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import Statement, Dormitory
from .serializers import StatementSerializer, DormitorySerializer


def index(request):
    return render(request, "main/index.html")


def statement_home(request):
    statements = Statement.objects.all()
    return render(request, "main/statements.html", {"statements": statements})


class StatementAPIListPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10000


class StatementViewSet(viewsets.ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer
    pagination_class = StatementAPIListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)


class DormitoryViewSet(viewsets.ModelViewSet):
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer

    @action(methods=["GET"], detail=False)
    def street(self, request):
        streets = Dormitory.objects.all()
        return Response({'street': [s.street for s in streets]})
