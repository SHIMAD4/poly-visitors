from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Statement, Dormitory
from .serializers import StatementSerializer, DormitorySerializer
from datetime import date


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
    permission_classes = (IsAuthenticated,)


class DormitoryViewSet(viewsets.ModelViewSet):
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer

    @action(methods=["GET"], detail=False)
    def street(self, request):
        streets = Dormitory.objects.all()
        return Response({'street': [s.street for s in streets]})

    @action(methods=['POST'], detail=True)
    def custom_action(self, request, pk=None):
        dormitory = self.get_object()
        new_description = request.data.get('new_description')
        if new_description:
            dormitory.description = new_description
            dormitory.save()
        return Response({'status': 'POST request handled for dormitory with id {}'.format(pk)})

    def get_queryset(self):
        condition1 = Q(street='Main Street') | Q(street='Broad Street')
        condition2 = Q(capacity__gt=50)

        combined_condition = condition1 & condition2

        queryset = Dormitory.objects.filter(combined_condition)
        return queryset
