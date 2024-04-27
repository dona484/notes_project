from typing import Any
from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title','text')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control my-3'}),
            'text' : forms.TextInput(attrs={'class':'form-control my-3'}),
        }
        labels = {
            'text':'write your thoughts'
        }


   # def clean_title(self):
    #   title = self.cleaned_data['title']
     #  if 'Django' not in title:
      #     raise forms.ValidationError('we only accept notes about django')
      # return title