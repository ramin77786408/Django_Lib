from django.urls import path
from . import views
import uuid

app_name = 'Lib'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('books/',views.BookListView.as_view(), name='book_list'),
    path('books/<int:pk>',views.BookDetailView.as_view(), name='book_detail'),
    path('authors/', views.AuthorListView.as_view(),name='authors'),
    path('mybooks/',views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('books/<int:pk>/borrow/', views.borrow_book, name='book-borrow'),
    path('mybooks/<uuid:pk>/renew/', views.renew_book_librarian, name='book-renew-librarian'),
]