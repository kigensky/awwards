from django.forms import ModelForm
from django.views.generic.edit import CreateView
from .models import Project, Rating
from captcha.fields import CaptchaField


class RatingCreateForm(ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = Rating
        exclude = ['creator', 'project', 'timestamp']

class ProjectCreateView(CreateView):
    model = Project
    fields = ['project name']