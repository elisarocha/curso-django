from django.shortcuts import render, redirect
from .models import Transação
from .form import TransaçãoForm
import datetime

def home(request):
    data = {}
    data['transações'] = ['t1', 't2', 't3']

    data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now

    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transações'] = Transação.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transação(request):
    data = {}
    form = TransaçãoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'contas/form.html', data)

def update(request, pk):
    data = {}
    transação = Transação.objects.get(pk=pk)
    form = TransaçãoForm (request.POST or None, instance=transação)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['transação'] = transação
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transação = Transação.objects.get(pk=pk)
    transação.delete()
    return redirect('url_listagem')