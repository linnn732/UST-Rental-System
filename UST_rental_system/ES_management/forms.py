from django import forms
from .models import Equipment

class AddEquModelForm(forms.ModelForm):
    
    class Meta:
        model = Equipment
        fields = ('name','usage','amount','price')
        
        #choices
        usage_choices = [('1','運動'), ('2','會議')]
    

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'usage': forms.Select(choices=(usage_choices), attrs={'class': 'form-select'}),
            'amount': forms.NumberInput(attrs={'min': '1'}),
            'price': forms.NumberInput(attrs={'min': '10'}),
        }
        
        labels = {
            'name': '名稱',
            'usage': '用途',
            'amount': '數量',
            'price': '價格',
        }