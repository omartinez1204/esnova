from django.forms import ModelForm
from serviciosapp.models import *

class usuarioForm(ModelForm):
    class Meta:
        model = usuario
        fields = ‘__all__’
