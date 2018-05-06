from django.db import models

class myinfo(models.Model):
	name=models.CharField(max_length=30)
	friends = models.CharField(max_length=4)
	profilepic = models.CharField(max_length=1000)

class myalbum(models.Model):
	album_title=models.CharField(max_length=40)
	album_logo=models.CharField(max_length=1000)
	photosnumber=models.CharField(max_length=10)
	profile =models.ForeignKey(myinfo,on_delete=models.CASCADE)

class photo(models.Model):
	caption = models.CharField(max_length=1000)
	album =models.ForeignKey(myalbum,on_delete=models.CASCADE)