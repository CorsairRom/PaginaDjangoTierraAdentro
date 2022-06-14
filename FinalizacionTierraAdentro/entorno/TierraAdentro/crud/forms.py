from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Contacto, Producto
from crud.Rut import validarRut
class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_consulta", "mensajes"]
        #fields = '__all__'
        
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ["nombre", "precio", "descripcion", "stock", "categoria", "imagen"]#nuevo
        exclude = ("usuario",)#nuevo

class Custom (UserCreationForm):
    pass

class ClienteForm(forms.ModelForm):
    fecha_nacimiento=forms.DateField(required=True,widget=forms.SelectDateWidget(attrs=({'style': 'width: 14%; display: inline;', 'class': 'mx-1'})))
    
    class Meta:
        model = Cliente
        field = ["nombre", "apellido", "rut", "direccion", "n_celular", "fecha_nacimiento"]
        exclude = ("usuario", "subscriptor", "vendedor",)
    
    def clean(self):
        super(ClienteForm, self).clean()
        ruts = self.cleaned_data.get('rut')
        if  validarRut(str(ruts)) == False:
            self.errors['rut'] = self.error_class(['Rut Invalido'])
        return self.cleaned_data
