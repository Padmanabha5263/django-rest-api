from django.urls import path
from . import views


urlpatterns = [
    path('', views.books, name="books-view"),
    path('<str:pk>/', views.bookDetile, name="perticular-book"),
]