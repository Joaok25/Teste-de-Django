from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Operation

User = get_user_model()

class CalculatorFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('alice', password='pass123')

    def test_requires_login(self):
        resp = self.client.get(reverse('calculator:index'))
        self.assertEqual(resp.status_code, 302)

    def test_create_operation(self):
        self.client.login(username='alice', password='pass123')
        self.client.post(reverse('calculator:index'), data={'a': '1', 'b': '2', 'op_type': 'ADD'})
        self.assertEqual(Operation.objects.filter(user=self.user).count(), 1)
        op = Operation.objects.first()
        self.assertEqual(str(op.result), '3')
