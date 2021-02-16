from django.forms import ModelForm
from serviciosapp.models import *
#from serviciosapp.models import Alumno
#class ArticuloAlumno(forms.Form):
#    articulos = forms.MultipleChoiceField(queryset=Articulo.objects.all(), label='articulos', required=True)
#    class Meta:
#        model = Alumno
#        fields = '[nombre,articulos]'
class usuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class UpArchivos(ModelForm):
    class Meta:
        model = subirArchivos
        fields = '__all__'
        exclude = ['usuario_fore']
