from decimal import Decimal, DivisionByZero
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from .forms import OperationForm
from .models import Operation
from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required
def index(request):
    form = OperationForm(request.POST or None)
    result = None
    if request.method == 'POST' and form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        op_type = form.cleaned_data['op_type']
        try:
            if op_type == Operation.OperationType.ADD:
                result = Decimal(a) + Decimal(b)
                symbol = '+'
            elif op_type == Operation.OperationType.SUB:
                result = Decimal(a) - Decimal(b)
                symbol = '-'
            elif op_type == Operation.OperationType.MUL:
                result = Decimal(a) * Decimal(b)
                symbol = '*'
            elif op_type == Operation.OperationType.DIV:
                if Decimal(b) == 0:
                    raise DivisionByZero('Divisão por zero não é permitida')
                result = Decimal(a) / Decimal(b)
                symbol = '/'
            else:
                messages.error(request, 'Operação inválida.')
        except DivisionByZero:
            messages.error(request, 'Divisão por zero não é permitida.')
        else:
            if result is not None:
                expr = f'{a} {symbol} {b}'
                Operation.objects.create(user=request.user, op_type=op_type, a=a, b=b, expression=expr, result=result)
                messages.success(request, f'Resultado: {result}')
    latest_ops = Operation.objects.filter(user=request.user)[:10]
    return render(request, 'calculator/index.html', {'form': form, 'latest_ops': latest_ops})

def custom_logout(request):
    logout(request)
    return redirect('login')
