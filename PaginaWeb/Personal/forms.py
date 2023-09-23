from django import forms

class Personal_form(forms.Form):

    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    dni = forms.IntegerField()
    fecha_nacimiento = forms.CharField(max_length=10)
    mail = forms.CharField(max_length=70)
    direccion = forms.CharField(max_length=100)
    localidad = forms.CharField(max_length=15)
    cp = forms.IntegerField()
    numero_contacto = forms.IntegerField()
    nombre_emergencia = forms.CharField(max_length=60)
    apellido_emergencia = forms.CharField(max_length=60)
    vinculo = forms.CharField(max_length=15)
    numero_contacto_emergencia = forms.IntegerField()
    sector = forms.CharField(max_length=15)
    permisos = forms.CharField(max_length=15)

class Usuario_form(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    user = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)

class Seller_form(forms.Form):
    cust_id = forms.IntegerField()
    nickname = forms.CharField(max_length=25)
    razon_social = forms.CharField(max_length=25)
    nombre_responsable = forms.CharField(max_length=20)
    apellido_responsable = forms.CharField(max_length=20)
    cotacto_resonsable = forms.EmailField(max_length=30)
    servicio_0 = forms.CharField(max_length=15)
    servicio_1 = forms.CharField(max_length=15)
    servicio_2 = forms.CharField(max_length=15)
    servicio_3 = forms.CharField(max_length=15)
    servicio_4 = forms.CharField(max_length=15)