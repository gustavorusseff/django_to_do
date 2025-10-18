from django.test import TestCase
from django.urls import reverse
from tarefas.models import Task

class FluxoBasicoTests(TestCase):
    def test_fluxo_criar_listar_concluir(self):
        list_url = reverse('tarefas:lista')
        
        r1 = self.client.get(list_url)
        self.assertContains(r1, 'Nenhuma tarefa ainda.')
        
        r2 = self.client.post(list_url, data={'title': 'Estudar testes'}, follow=True)

        self.assertEqual(r2.status_code, 200)
        self.assertContains(r2, 'Estudar testes')
        tarefa = Task.objects.get(title='Estudar testes')
        self.assertFalse(tarefa.done)
        
        toggle_url = reverse('tarefas:toggle', args=[tarefa.pk])
        r3 = self.client.post(toggle_url, follow=True)
        self.assertEqual(r3.status_code, 200) 
        
        tarefa.refresh_from_db()
        self.assertTrue(tarefa.done)

        self.assertContains(r3, 'Desfazer')