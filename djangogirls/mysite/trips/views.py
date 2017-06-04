
# Create your views here.


from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render




def hello_world(request):
	return render(request, 'hello_world.html', {'current_time': str(datetime.now()),})




def view_(request):
	#return HttpResponse("THIS IS VIEW ONE!")
	return render(request, 'd3_test.html')
