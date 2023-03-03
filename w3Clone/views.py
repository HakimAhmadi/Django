from django.shortcuts import render, loader
from django.http import request
from django.shortcuts import get_object_or_404
from .models import Python


# Create your views here.
def main(request):

    data = Python.objects.all()
    return render(request, 'base.html', {'data': data})


def topic(request, pk):
    # topic = get_object_or_404(Python, id=pk)
    data = Python.objects.all()
    id = Python.objects.get(id=pk)

    return render(request, 'main.html', {"data": data, "id": id.text})