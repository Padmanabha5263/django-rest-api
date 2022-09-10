from django.urls import path
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    path('books/', views.books, name="books"),
    path('books/<str:pk>/', views.bookDetile, name="perticular-book"),

    path('authors/', views.authors, name="authors"),
    path('authors/<str:pk>/', views.author, name="perticular-author"),

    path('publications/', views.publications, name="publications"),
    path('publications/<str:pk>/', views.publication, name="perticular-publication"),

    path('', RedirectView.as_view(url="books/"))
]