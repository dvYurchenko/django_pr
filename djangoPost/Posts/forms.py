from django.forms import ModelForm
from django.template.defaultfilters import title
from .models import Posts

class PostForm(ModelForm):
    class Meta:
        model=Posts
        fields = ['title', 'content', 'author']