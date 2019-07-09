from django.shortcuts import render
from rest_framework import generics 
from .serializers import BucketlistSerializer
from .models import Bucketlist

# Create your views here.
class CreateView(generics.ListCreateAPIView):
	queryset = Bucketlist.objects.all()
	serializers_class = BucketlistSerializer

	def perform_create(self, serializers):
		serializers.save()
