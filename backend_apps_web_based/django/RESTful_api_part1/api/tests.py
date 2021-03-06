from django.test import TestCase
from .models import Bucketlist 
from rest_framework.test import APIClient 
from rest_framework import status 
from django.urls import reverse 

# Create your tests here.
class ModelTestCase(TestCase):

	def setUp(self):
		self.bucketlist_name = "my bucketlist"
		self.bucketlist = Bucketlist(name=self.bucketlist_name)

	def test_model_can_create_a_bucketlist(self):
		old_count = Bucketlist.objects.count()
		self.bucketlist.save()
		new_count = Bucketlist.objects.count()
		self.assertNotEqual(old_count, new_count)

class viewTestCase(TestCase):

	def setUp(self):
		self.client = APIClient()
		self.bucketlist_data = {'name': 'go to NYC'}
		self.response = self.client.post(
			reverse('create'),
			self.bucketlist_data,
			format="json")

	def test_api_can_create_a_bucketlist(self):
		self.assertEqual(self.response.status_code,status.HTTP_201_CREATED)
