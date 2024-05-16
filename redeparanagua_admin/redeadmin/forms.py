from django import forms
from .models import Servicos
from decimal import Decimal


class ServicosForm(forms.ModelForm):
    porcentagem = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    preco_maximo = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    preco_minimo = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    class Meta:
        model = Servicos
        fields = '__all__'

    def clean_porcentagem(self):
        data = self.cleaned_data['valor_minimo']
        return Decimal(data.replace(',',','))

    def clean_preco_minimo(self):
        data = self.cleaned_data['valor_minimo']
        return Decimal(data.replace(',',','))
    
    def clean_preco_maximo(self):
        data = self.cleaned_data['valor_minimo']
        return Decimal(data.replace(',',','))
