from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Server (models.Model):
    idServerDetails = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    serverAddress = models.URLField()
    serverUsername = models.CharField(max_length=128)
    serverPassword = models.CharField(max_length=128)
    dateAdded = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.serverAddress

class Authentication(models.Model):
    idAuthentication = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    organisation = models.CharField(max_length=128)

    def __unicode__(self):
        return "%s %s" %(self.username,self.organisation)

class Jobs(models.Model):
    idJobs = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    jobName = models.CharField(max_length=128)
    boxID = models.CharField(max_length=128)
    captricityID = models.CharField(max_length=128)
    serverAddress = models.ForeignKey(Server,related_name='address')
    idserverDetails = models.ForeignKey(Server,related_name='ServerDetails')
    location = models.CharField(max_length=128)
    identifier = models.CharField(max_length=128)
    encounterType = models.CharField(max_length=128)
    dateCreated = models.DateField(auto_now_add=True)
    #jobImage= models.ImageField()

    def __unicode__(self):
        return "%s %s" %(self.jobName,self.dateCreated)

class JobStatus(models.Model):
    idJobStatus = models.AutoField(primary_key=True)
    idJobs = models.ForeignKey(Jobs)
    jobStatus = models.CharField(max_length=128)
    dateUpdated = models.DateField()
    retired = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s" %(self.idJobs,self.jobStatus)

class Shredder(models.Model):
    idShredder = models.AutoField(primary_key=True)
    idJobs = models.ForeignKey(Jobs)
    idCSV = models.FileField(upload_to='documents/%Y/%m/%d')
    shredderStatus = models.CharField(max_length=128)

    def __unicode__(self):
        return "%s %s" %(self.idShredder,self.shredderStatus)

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    #additional models we wish to include
    website = models.URLField(blank=True)
    middle_name = models.CharField(max_length=128, blank=True)
    DOB = models.DateField()
    sex = models.CharField(max_length=128,blank=True)
    country = models.CharField(max_length=128,blank=True)
    organisation = models.CharField(max_length=128)
    #picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')