from django.db import models


class Numbers(models.Model):
	"""
	database table for roman-arabic numbers
	"""
	roman = models.CharField(max_length=5)
	arabic = models.IntegerField()

	class Meta:
		ordering = ["-arabic"]

	def __str__(self):
		return "{0} {1}".format(self.roman, self.arabic)

class History(models.Model):
	"""
	save history of conversion
	revrite oldest one
	"""
	from_num = models.CharField(max_length=128)
	to_num = models.CharField(max_length=128)
	time = models.TimeField()

	class Meta:
		ordering = ["-time"]
		get_latest_by = ["-time"]
