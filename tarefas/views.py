from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.mail import send_mail # Importação OK
from .models import Task
from .forms import TaskForm

def task_list_create(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            
            send_mail(
                subject='Nova tarefa criada',
                message=f'Você criou: {task.title}',
                from_email='noreply@example.com',
                recipient_list=['admin@example.com'],
                fail_silently=True
            )
            
            return redirect('tarefas:lista')
    else:
        form = TaskForm()

    return render(request, 'tarefas/lista.html', {'form': form, 'tasks': tasks})

@require_POST
def toggle_done(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save(update_fields=['done'])
    return redirect('tarefas:lista')