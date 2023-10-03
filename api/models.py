from django.db import models
from rest_framework import serializers
import random
from accounts.models import User
# Create your models here.

class Peeps(models.Model):

    name = models.CharField(max_length=16, blank=False, editable=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    seed = models.IntegerField(blank=True, editable=False, unique=True)

    users = models.ManyToManyField(User, related_name="users")

    def save(self, *args, **kwargs): 
        if not self.seed: 
            while True:
                seed = random.randint(1000000, 1999999)

                if not Peeps.objects.filter(seed=seed).exists():
                    
                    self.seed = seed

                    break
        
        self.name = self.name.lower().replace(' ', '_')

        super().save(*args, **kwargs)


class PeepsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Peeps
        fields = '__all__'