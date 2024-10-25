from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('username', 'email', 'content',)
        labels = {
            # 'username': 'Your username: ',
            'email': 'Your e-mail address:',
            'content': 'Comment:'
        }
        error_messages = {
            'username': {
                'required': 'Your username must not be empty',
                'max_length': 'Please use a username shorter than 64 characters',
            }
        }
