from django.db import models

class VocabItem(models.Model):
	"""
	Vocab Item Model
	"""

	word = models.CharField(max_length=512, unique=True, db_index=True)

	origin = models.TextField(null=True, blank=True)
