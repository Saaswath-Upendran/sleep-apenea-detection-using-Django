from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # email = models.EmailField()

    def __str__(self):
        self.user.username


class AImodel(models.Model):
    """
    
    age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal	target
    """
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField()
    tresbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.IntegerField()
    exang = models.IntegerField()
    oldpeak = models.IntegerField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()



