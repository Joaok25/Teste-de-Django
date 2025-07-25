from django.conf import settings
from django.db import models

class Operation(models.Model):
    class OperationType(models.TextChoices):
        ADD = 'ADD', 'Soma'
        SUB = 'SUB', 'Subtração'
        MUL = 'MUL', 'Multiplicação'
        DIV = 'DIV', 'Divisão'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='operations')
    op_type = models.CharField(max_length=3, choices=OperationType.choices)
    a = models.DecimalField(max_digits=20, decimal_places=6)
    b = models.DecimalField(max_digits=20, decimal_places=6)
    expression = models.CharField(max_length=255)
    result = models.DecimalField(max_digits=20, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user} -> {self.expression} = {self.result}'
    