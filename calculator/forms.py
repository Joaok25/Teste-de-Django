from django import forms
from .models import Operation

class OperationForm(forms.Form):
    a = forms.DecimalField(label='A', required=True)
    b = forms.DecimalField(label='B', required=True)
    op_type = forms.ChoiceField(label='Operação', choices=Operation.OperationType.choices)
