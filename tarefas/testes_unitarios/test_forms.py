from django.test import SimpleTestCase
from tarefas.forms import TaskForm

class TaskFormTests(SimpleTestCase):
    def test_form_valido_quando_titulo_ok(self):
        form = TaskForm(data={'title': 'Comprar pão'})
        self.assertTrue(form.is_valid())
        self.assertNotIn('title', form.errors)

    def test_form_invalido_quando_titulo_curto(self):
        form = TaskForm(data={'title': 'Oi'})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)