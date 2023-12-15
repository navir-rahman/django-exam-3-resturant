from django.shortcuts import render

# Create your views here.

from static import mealdata
def index(request):
    return render(request, 'index.html', {'meal': mealdata.categories})