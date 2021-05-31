from django.forms import ModelForm
# from django.views.generic.edit import CreateView
from .models import Rating
from captcha.fields import CaptchaField


class RatingCreateForm(ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = Rating
        exclude = ['creator', 'project', 'timestamp']
