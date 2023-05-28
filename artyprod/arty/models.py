from django.db import models
from datetime import datetime

class Project(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    date_creation = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='images/')
    temoignage = models.TextField() 

    def __str__(self):
        return self.nom

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

class Equipe(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    personnel = models.CharField(max_length=50)

    def __str__(self):
        return self.nom
    

    
from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator

class Membre(models.Model):
    name = models.CharField(max_length=255)
    cv = models.FileField(upload_to='cvs/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])
    image = models.ImageField(upload_to='images/')
    linkedin = models.URLField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Membre, self).save(*args, **kwargs)
        
class Service(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.nom
