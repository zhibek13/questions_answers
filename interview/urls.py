from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    # path('', include(router.urls)),
    path('categorys/', views.CategoryCreateListView.as_view(), name='news-create-list'),
    path('categorys/<int:category_id>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='news-retrieve-update-destroy'),
    path('questions/', views.QuestionAnswerCreateListView.as_view(), name='news-create-list'),
    path('questions/<int:question_id>/', views.QuestionAnswerRetrieveUpdateDestroyAPIView.as_view(), name='news-retrieve-update-destroy'),
]