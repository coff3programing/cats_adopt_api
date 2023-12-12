from django.db import models

# Create your models here.
class Cats(models.Model):
    catName= models.CharField(max_length=60)
    gender = models.CharField(max_length=22);
    size= models.CharField(max_length=15)
    breed= models.CharField(max_length=64)
    age = models.IntegerField();
    adoptionStatus= models.BooleanField(default=False)
    personality= models.TextField(blank=True)

    def __str__(self) :
        return self.catName
