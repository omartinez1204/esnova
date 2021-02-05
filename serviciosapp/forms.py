from django.forms import ModelForm
from serviciosapp.models import Alumno
class ArticuloAlumno(forms.Form):
    articulos = forms.MultipleChoiceField(queryset=Articulo.objects.all(), label='articulos', required=True)
    class Meta:
        model = Alumno
        fields = '[nombre,articulos]'

class UpArchivos(ModelForm):
    class Meta:
        model = subirArchivos
        fields = '__all__'
