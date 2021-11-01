from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from TodoApp.models import Todo

class TodoForm(ModelForm):
    class Meta:
        model =Todo
        fields= ['title', 'desc', 'status']
        widgets =  {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'desc'  : forms.Textarea(attrs={'class': 'form-control'}),  
            'status': forms.Select(attrs={'class': 'form-control'})
        }