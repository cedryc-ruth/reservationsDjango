from django.db import models

# Create your models here.
class Artist(models.Model):
	firstname = models.CharField(max_length=60)
	lastname = models.CharField(max_length=60)
	
	class Meta:
		db_table = "artists"

class Type(models.Model):
	type = models.CharField(max_length=60)
	
	class Meta:
		db_table = "types"
	
class Locality(models.Model):
	postal_code = models.CharField(max_length=6)
	locality = models.CharField(max_length=60)
	
	class Meta:
		db_table = "localities"

class Role(models.Model):
	role = models.CharField(max_length=30)
	
	class Meta:
		db_table = "roles"
