from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    comment = forms.CharField(label="", widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Write your opinion',
        'id': 'usercomment',
        'rows':'4'
    }))
    class Meta:
        model = Comment
        fields = ('comment',)