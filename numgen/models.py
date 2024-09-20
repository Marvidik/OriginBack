from django.db import models

# Create your models here.



class Token(models.Model):

    key=models.CharField(max_length=100)


class State(models.Model):
    state=models.CharField(max_length=100)

    def __str__(self):

        return self.state

class Numbers(models.Model):
    stat=models.ForeignKey(State,on_delete=models.CASCADE)
    num=models.CharField(max_length=16)


    def __str__(self):

        return self.num




