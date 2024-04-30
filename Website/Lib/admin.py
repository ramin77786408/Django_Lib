from django.contrib import admin
from . import models

admin.site.register(models.Book)
admin.site.register(models.BookInstance)
admin.site.register(models.Author)
admin.site.register(models.Genre)

class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = [
        ("Information", {'fields': ['book','imprint','id']}),
        ('Availability', {'fields': ['status','due_back']}),
    ]

class BookInstanceInline(admin.TabularInline):
    model = models.BookInstance
    extra = 1

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'author']}),
        ('Date information', {'fields': ['publication_date']}),
    ]
    inlines = [BookInstanceInline]


class AuthorAdmin(admin.ModelAdmin):
    fields = ['first_name','last_name',('date_of_birth','date_of_death')]
    


