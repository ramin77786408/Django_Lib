from typing import Any
from django.shortcuts import render
from django.views import generic
from . import models

# def index(request,):
#     num_books = models.Book.objects.all().count()
#     num_instances = models.BookInstance.objects.all().count()
#     num_instances_available = models.BookInstance.objects.filter(status__exact='a').count()
#     num_authors = models.Author.objects.count()

#     return render(
#         request,
#         'lib/index.html',
#         context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
#     )

class Index(generic.TemplateView):
    template_name = 'lib/index.html'

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['num_books'] = models.Book.objects.all().count()
        context['num_instances'] = models.BookInstance.objects.all().count()
        context['num_instances_available'] = models.BookInstance.objects.filter(status__exact='a').count()
        context['num_authors'] = models.Author.objects.count()
        return context
    
class BookListView(generic.ListView):
    model = models.Book
    template_name = 'lib/book_list.html'


class BookDetailView(generic.DetailView):
    model = models.Book
    template_name = 'lib/book_detail.html'