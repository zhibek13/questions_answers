from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    # path('', include(router.urls)),
    path('categorys/', views.CategoryCreateListView.as_view(), name='news-create-list'),
    path('categorys/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='news-retrieve-update-destroy'),
    path('questions/', views.QuestionAnswerCreateListView.as_view(), name='news-create-list'),
    path('questions/<int:pk>/', views.QuestionAnswerRetrieveUpdateDestroyAPIView.as_view(), name='news-retrieve-update-destroy'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)