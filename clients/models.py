from django.conf import settings
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=150, unique=True)
    project_title = models.CharField(max_length=150)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        
class ClientNote(models.Model):
    client = models.ForeignKey(Client)
    note_title = models.CharField(max_length=150, unique=True)
    note = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return '%s - %s' % (self.client, self.note_title)
    
    class Meta:
        ordering = ('note_title', 'client')
    
class Contact(models.Model):
    name = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    primary_phone = models.CharField(max_length=20)
    secondary_phone = models.CharField(max_length=20, blank=True, null=True)
    client = models.ForeignKey(Client)
        
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name', 'client')
    
class Access(models.Model):
    client = models.ForeignKey(Client)
    access_type = models.CharField(max_length=150)
    url = models.URLField(max_length=150, blank=True, null=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    note = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return '%s - %s' % (self.client, self.access_type)
    
    class Meta:
        ordering = ('client', 'access_type')
        verbose_name_plural = 'Access'
        
class AccessNote(models.Model):
    access = models.ForeignKey(Access)
    note_title = models.CharField(max_length=150, unique=True)
    note = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return '%s - %s' % (self.access, self.note_title)
    
    class Meta:
        ordering = ('access', 'note_title')