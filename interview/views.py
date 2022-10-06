from django.shortcuts import render
from django.db import IntegrityError
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, \
    get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CategorySerializer, QuestionAnswerSerializer, QuestionsAnswersSerializer
from .models import Category, QuestionAnswer


class CategoryCreateListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(name=self.request.name)


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerCreateListView(ListCreateAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer

    def get_queryset(self):
        queryset = QuestionAnswer.objects.order_by('-importance')
        return queryset

    def perform_create(self, serializer):
        serializer.save(name=self.request.name)


class QuestionAnswerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionsAnswersSerializer
