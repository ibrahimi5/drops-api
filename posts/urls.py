from django.urls import path
from .views import PostShowView, PostDetailView

urlpatterns = [
    path('', PostShowView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
]