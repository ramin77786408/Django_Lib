from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime
from . import models

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        date = self.cleaned_data["renewal_date"]

        if date < datetime.date.today():
            raise ValidationError(_('Invalid date - renwal in past'))
        if date > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        return date
    
class GetBookForm(forms.ModelForm):
    
    class Meta:
        model = models.BookInstance
        fields = ['imprint','due_back', ]

    
