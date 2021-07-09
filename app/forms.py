from django import forms
from .models import TODOModel

class TODOForm(forms.ModelForm):
    class Meta:
        model = TODOModel
        fields = "__all__"