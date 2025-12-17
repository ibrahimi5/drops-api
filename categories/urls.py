from django.urls import path
from .views import CategoryIndexView, PostByCategoryView

urlpatterns = [
    path('', CategoryIndexView.as_view()),
    path('<int:pk>/posts/',  PostByCategoryView.as_view()),
]