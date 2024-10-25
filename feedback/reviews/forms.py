from django import forms

from .models import Review


# class ReviewForm(forms.Form):
#     username = forms.CharField(
#         label='Your name', min_length=3, max_length=32, required=True,
#         error_messages={'required': 'Your name must not be empty',
#                         'min_length': 'Please enter username longer than 3 characters'})
#     text = forms.CharField(label='Your feedback:', widget=forms.Textarea, max_length=256)
#     rating = forms.IntegerField(label='Your rating:', min_value=1, max_value=10)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('username', 'text', 'rating')  # '__all__'
        # exclude = ('something',)
        labels = {
            'username': 'Your name: ',
            'text': 'Your feedback:',
            'rating': 'Your rating:'
        }
        error_messages = {
            'username': {
                'required': 'Your username must not be empty',
                'max_length': 'Please use a username shorter than 32 characters',
            }
        }
