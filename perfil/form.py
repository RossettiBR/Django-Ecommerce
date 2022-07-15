from django import forms
from django.contrib.auth.models import User
from .models import Perfil


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        exclude = ('usuario',)


class Userform(forms.ModelsForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',
                  'password'
                  )

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        return self.clean(*args, **kwargs)
