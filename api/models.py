from django.db import models
from rest_framework import serializers
import random
from accounts.models import User
from django.core.validators import MaxValueValidator

# Create your models here.

class Peeps(models.Model):

    name = models.CharField(max_length=16, blank=False, editable=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    seed = models.IntegerField(blank=True, editable=False, unique=True)

    users = models.ManyToManyField(User, related_name="users")

    hp = models.SmallIntegerField(editable=False, default=100)
    
    age = models.SmallIntegerField(editable=False, default=0)

    # attributes

    attribute_creativity = models.FloatField(editable=False, default=0)
    attribute_romance = models.FloatField(editable=False, default=0)
    
    def save(self, *args, **kwargs): 
        if not self.seed: 
            while True:
                seed = random.randint(1000000, 1999999)

                if not Peeps.objects.filter(seed=seed).exists():
                    
                    self.seed = seed

                    break
        
        self.name = self.name.lower().replace(' ', '_')
        if self.attribute_creativity == 0 and self.attribute_romance == 0:
            random.seed(self.seed)
            self.attribute_creativity = round(random.uniform(0, 0.5), 3)
            self.attribute_romance = round(random.uniform(0, 0.5), 3)

        super().save(*args, **kwargs)

class PeepsMetric(models.Model):
    time = models.DateTimeField(auto_now_add=True, db_index=True, primary_key=True)
    action = models.CharField(max_length=255)
    peep = models.ForeignKey(Peeps, on_delete=models.CASCADE)
    hp = models.IntegerField()
    attribute_creativity = models.FloatField()
    attribute_romance = models.FloatField()

    

class PeepsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Peeps
        fields = '__all__'