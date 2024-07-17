from django.shortcuts import render
from .models import Room

# Create your views here.

# services = [
#     {'id':1, 'name':'Insurance', 'description': '$20,000'},
#     {'id':2, 'name':'Healthsend', 'description': '$320,000'},
#     {'id':3, 'name':'Fulfilment', 'description': '$2,520,000'},
# ]



def home(request):
    services = Room.objects.all()
    context = {'services': services}
    return render(request, 'base_app/home.html', context)

def room(request, pk):
    service = Room.objects.get(id=pk)
    context = {'service': service}
    return render(request, 'base_app/room.html', context)