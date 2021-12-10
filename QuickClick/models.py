from django.db import models

# Create your models here.
class Attempt(models.Model) :
    score = models.IntegerField(default=0)
    name = models.CharField(max_length=3)

    def __str__(self) :
        return (self.name)
    
    def save(self) :
        self.name = self.name.upper()
        super(Attempt, self).save()