from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
import datetime
from .forms import RenewBookForm

from django.urls import reverse


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

class AuthorListView(generic.ListView):
    model = models.Author
    template_name = 'lib/author_list.html'


class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = models.BookInstance
    template_name = 'lib/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return models.BookInstance.objects.filter(borrower=self.request.user).filter(
            status__exact='o').order_by('due_back')
    


# @permission_required('Lib.can_mark_returned')
def renew_book_librarian(request, pk):
    
    book_instance = get_object_or_404(models.BookInstance, pk=pk)
    
    if(request.method == 'POST'):
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()
            return HttpResponseRedirect(reverse('Lib:my-borrowed'))
    else:
        proposed = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed})

    return render(request, 'lib/book_renew_librarian.html', {'form': form, 'book_instance': book_instance})
    