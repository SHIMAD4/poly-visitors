# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import EmailSerializer, StatementSerializer, DormitorySerializer
from .models import Statement, Dormitory


# Главная страница
def index(request):
    return render(request, "main/index.html")


# Страница заявлений
def statement_home(request):
    statements = Statement.objects.all()
    return render(request, "main/statements.html", {"statements": statements})


# Страница настроек
def settings_home(request):
    return render(request, "main/settings.html")


# Страница отправки email
def settings_mail(request):
    return render(request, "main/mail.html")


# Класс для отправки email
class EmailViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def send_email(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']
            recipient = serializer.validated_data['recipient']

            try:
                send_mail(
                    subject,
                    message,
                    'your-email@example.com',
                    [recipient],
                    fail_silently=False,
                )
                return Response({'status': 'success'}, status=status.HTTP_200_OK)
            except UnicodeDecodeError as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Пагинация для API заявлений
class StatementAPIListPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = "page_size"
    max_page_size = 10000


# ViewSet для заявлений
class StatementViewSet(viewsets.ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer
    pagination_class = StatementAPIListPagination
    permission_classes = (IsAuthenticated,)


# ViewSet для общежитий
class DormitoryViewSet(viewsets.ModelViewSet):
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer

    @action(methods=["GET"], detail=False)
    def street(self, request):
        streets = Dormitory.objects.all()
        return Response({"street": [s.street for s in streets]})

    @action(methods=["POST"], detail=True)
    def custom_action(self, request, pk=None):
        dormitory = self.get_object()
        new_description = request.data.get("new_description")
        if new_description:
            dormitory.description = new_description
            dormitory.save()
        return Response(
            {"status": f"POST request handled for dormitory with id {pk}"}
        )
