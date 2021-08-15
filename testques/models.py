from django.db import models

# Create your models here.

class Question(models.Model):
	"""
	Model for saving Questions in database
	"""
	question_text = models.CharField(max_length=300)
	

	def __str__(self):
		"""
		String representation of the object
		"""
		return self.question_text


class Option(models.Model):
	"""
	Option model for question having a OneToMany Relationship with 
	Question Mode
	"""
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	option_text = models.CharField(max_length=200)

	def __str__(self):
		"""
		String representation of the object
		"""
		return self.option_text



class Group(models.Model):
	"""
	Group model having multiple question to form a group
	"""
	group_name = models.CharField(max_length=100)
	question = models.ManyToManyField(Question)
	
	def __str__(self):
		"""
		String representation of the object
		"""
		return self.group_name