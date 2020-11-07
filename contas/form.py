from django.forms import ModelForm
from .models import Transação

class TransaçãoForm(ModelForm):
    class Meta:
        model = Transação
        fields = ['data', 'descrição', 'valor', 'observações', 'categoria']
