from .models import Members
from django.forms import ModelForm


class MembersForm(ModelForm):
    class Meta:
        model = Members
        fields = ['name','chai_or_coffee']