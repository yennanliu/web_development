
# Create your views here.


from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render




def hello_world(request):
	return render(request, 'hello_world.html', {'current_time': str(datetime.now()),})