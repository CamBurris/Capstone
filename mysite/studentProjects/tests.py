from django.test import TestCase
from studentProjects.models import Project, Student, ExtraForm
from django.test.client import Client

# Create your tests here.
class StudentProjectTestCase(TestCase):
	#def setUp(self):
	#	ExtraForm.objects.create(name='a',link='http://youtube.com',required=False,description='asdf')
	
	def test_forms(self):
		resp = self.client.get('/forms/')
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('otherForms' in resp.context)
	
	def test_create(self):
		resp = self.client.get('/create/')
		self.assertEqual(resp.status_code, 200)