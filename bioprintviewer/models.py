from django.db import models
#from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField
from django_mongodb_engine.contrib import MongoDBManager

# Create your models here.
class User_Info(models.Model):
    email = models.TextField()
    serial = models.IntegerField()

class Print_Data(models.Model):
    livePercent = models.FloatField()
    elasticity = models.FloatField()
    deadPercent = models.FloatField()

class Crosslinking(models.Model):
    cl_enabled = models.BooleanField()
    cl_duration = models.IntegerField()
    cl_intensity = models.IntegerField()

class Files(models.Model):
    input = models.TextField()
    output = models.TextField()

class Pressure(models.Model):
    extruder1 = models.FloatField()
    extruder2 = models.FloatField()

class Resolution(models.Model):
    layerNum = models.IntegerField()
    layerHeight = models.FloatField()

class Print_Info(models.Model):
    crosslinking = EmbeddedModelField('Crosslinking')
    files = EmbeddedModelField('Files')
    pressure = EmbeddedModelField('Pressure')
    resolution = EmbeddedModelField('Resolution')
    wellplate = models.IntegerField()

class BioPrint(models.Model):
    user_info = EmbeddedModelField('User_Info')
    print_data = EmbeddedModelField('Print_Data')
    print_info = EmbeddedModelField('Print_Info')
    objects = MongoDBManager()
