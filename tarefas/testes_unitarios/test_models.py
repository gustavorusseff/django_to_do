
from django.core.exceptions import ValidationError
from django.test import TestCase
from tarefas.models import Task

class TaskModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.t1 = Task.objects.create(title='Estudar Django')
        cls.t2 = Task.objects.create(title='Escrever testes', done=True)

    def test_str_mostra_status_e_titulo(self):
        self.assertEqual(str(self.t1), '[X) Estudar Django')
        self.assertEqual(str(self.t2), '[) Escrever testes')

    def test_mark_done_marca_e_persiste(self):
        t = Task.objects.create(title='Aprender coverage')
        self.assertFalse(t.done)
        t.mark_done()
        t.refresh_from_db()
        self.assertTrue(t.done)

    def test_title_precisa_ter_minimo_de_caracteres(self):
        t = Task(title='01')
        with self.assertRaises(ValidationError):
            t.full_clean()

    def test_ordering_por_created_at_desc(self):
        lista = list(Task.objects.all())
        self.assertEqual(lista, [self.t2, self.t1])