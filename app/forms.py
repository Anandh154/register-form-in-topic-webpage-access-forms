from app.models import *
from django import forms

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','url','picture']
        
class AccessRecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields=['date','author','author_pic']
