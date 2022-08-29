from django.db import models
from django.utils import timezone

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_date = models.DateField()

    def __str__(self):
        return '%s' % self.name 

    def save(self,*args,**kwargs):
        if not self.id:
            self.created_date = timezone.now()

        return super(Users,self).save(*args,**kwargs)

    def check_password(self):
        if self.password:
            if len(self.password)<5:
                return False
        return True