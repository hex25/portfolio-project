from django.db import models

# Create your models here.

class Blog(models.Model):
	
	title = models.CharField(max_length=100)
	publ_date = models.DateTimeField()
	summary = models.TextField() 
	image = models.ImageField(upload_to='images/') 

	def shortsummary(self):
		return self.summary[:100]

	def publ_date_pretty(self):
		return self.publ_date.strftime('%b %e %Y')

	def __str__(self):
		return self.title