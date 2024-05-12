from django.urls import path
from . import views

app_name = 'Lib'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('books/',views.BookListView.as_view(), name='book_list'),
    path('books/<int:pk>',views.BookDetailView.as_view(), name='book_detail'),
    path('authors/', views.AuthorListView.as_view(),name='authors'),
]