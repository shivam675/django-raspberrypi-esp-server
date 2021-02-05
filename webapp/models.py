from django.db import models

# Create your models here.
class room(models.Model):
	"""docstring for room"""
	room_name = models.CharField(max_length=100)
	Number_of_switchboard = models.PositiveSmallIntegerField()
	def __str__(self):
		km = self.room_name + ' ------------------------ ' + str(self.Number_of_switchboard)
		return km

class switchboard(models.Model):
	switchboard_number = models.PositiveSmallIntegerField()
	IP_of_switchboard = models.CharField(max_length=100)
	def __str__(self):
		jm = self.IP_of_switchboard + ' -------------- Number : ' + str(self.switchboard_number)
		return jm